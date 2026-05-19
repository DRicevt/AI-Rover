# AI Rover

AI Rover is a proof-of-concept physical AI rover for real-world autonomy research. The platform is being designed around a Jetson Orin Nano 8GB, camera, and time-of-flight sensing so it can perceive and navigate unknown terrain while keeping compute on the vehicle.

The long-term control stack pairs a local LLM for high-level reasoning with conventional deterministic computing for low-level control. As the platform matures, reinforcement learning is planned for low-level decision making so the rover can improve local motion behavior, obstacle response, and terrain handling through simulation and physical testing.

## Project Goals

| Goal | Description | Status |
| --- | --- | --- |
| Edge AI autonomy | Run high-level navigation and mission reasoning locally on the Jetson Orin Nano 8GB. | Planned |
| Sensor-driven navigation | Use camera data and ToF depth data for obstacle awareness and terrain understanding. | ToF bring-up in progress |
| Layered control | Separate high-level planning from low-level motor, sensor, and safety control. | Architecture in progress |
| Repeatable subsystem testing | Bring up every sensor, actuator, and support circuit independently before full integration. | Active |
| Printable mechanical design | Build a full Fusion 360 CAD model that can be manufactured with 3D printing. | Planned |
| Hardware documentation | Publish mechanical, electrical, and test/manufacturing BOMs as the design stabilizes. | Planned |

## Current Progress

The repository is currently in the subsystem bring-up phase. Each hardware block is tested in isolation first, documented, and then promoted into the future integrated rover stack once it is understood and repeatable.

| Subsystem | Current Work | Documentation |
| --- | --- | --- |
| VL53L5CX ToF sensor | Raspberry Pi Pico firmware reads an 8x8 distance grid over I2C and streams frames over USB serial. A Python tool renders the data as a live heat map. | [ToF bring-up guide](Rover/Bringup/ToF/README.md) |
| DHT11 environmental sensor | Raspberry Pi Pico firmware reads temperature and humidity and prints values over USB serial. | [DHT11 bring-up guide](Rover/Bringup/DHT11/README.md) |
| Embedded firmware | PlatformIO project with separate environments for each bring-up target. | [Rover firmware](Rover/README.md) |
| Electrical design | KiCad project for the main rover electronics. | [KiCad/Rover_main](KiCad/Rover_main) |
| Mechanical design | Fusion 360 rover CAD model planned for printable chassis, mounts, and electronics packaging. | Image/link pending |
| System integration | Integration will begin after the individual bring-up targets are tested and documented. | Planned |

## System Architecture

The rover is being built as a layered system so each responsibility has a clear boundary:

| Layer | Responsibility | Planned Components |
| --- | --- | --- |
| Mission / reasoning | Interpret goals, choose high-level actions, decide when to explore, stop, retry, or ask for help. | Local LLM on Jetson Orin Nano |
| Perception | Convert camera and ToF data into useful world/context signals. | Camera, VL53L5CX ToF sensor, future perception models |
| Navigation | Turn high-level goals and perception into local path choices. | Classical planning first, RL integration later |
| Low-level control | Drive motors, read sensors, enforce timing and safety limits. | Microcontroller firmware, motor drivers, sensor buses |
| Power and electrical | Distribute power safely and connect compute, sensors, and actuators. | Custom KiCad electronics, wiring harnesses, protection |
| Mechanical platform | Hold drivetrain, sensors, Jetson, batteries, and electronics in a printable rover body. | Fusion 360 CAD, 3D printed parts |

```text
High-level goal / user command
        |
        v
Local LLM on Jetson Orin Nano
        |
        v
Navigation and perception software
        |
        v
Low-level control firmware
        |
        v
Motors, sensors, power, and mechanical rover body
```

> Figure needed: overall rover system architecture diagram.

## Bring-Up First Engineering Approach

This project uses a bring-up-first systems engineering workflow:

1. Define the subsystem boundary and expected behavior.
2. Wire and test the subsystem on the bench.
3. Write minimal firmware or host tooling to prove the subsystem works.
4. Document wiring, commands, expected output, and common failure modes.
5. Repeat until the result is stable enough to integrate.
6. Begin rover-level integration only after the major subsystems have passed individual tests.

This keeps electrical, firmware, mechanical, and autonomy problems from being mixed together too early. The goal is to make failures small, observable, and fixable before the full rover stack is assembled.

## Bring-Up Examples

### VL53L5CX ToF Sensor

The ToF bring-up reads an 8x8 grid of distance values from the VL53L5CX and streams it over USB serial. A Python viewer converts the serial frames into a live heat map for quick sensor validation.

| Serial 8x8 Grid | Live Heat Map |
| --- | --- |
| ![8x8 distance grid in the serial monitor](Rover/Bringup/ToF/images/8x8_grid.png) | ![VL53L5CX distance heat map](Rover/Bringup/ToF/images/heat_map.png) |

Guide: [Rover/Bringup/ToF/README.md](Rover/Bringup/ToF/README.md)

### DHT11 Temperature and Humidity Sensor

The DHT11 bring-up verifies a simple environmental sensor path using Pico firmware and USB serial output.

![DHT11 serial monitor output](Rover/Bringup/DHT11/images/dht11_output.png)

Guide: [Rover/Bringup/DHT11/README.md](Rover/Bringup/DHT11/README.md)

## Mechanical Design

A full 3D CAD model will be developed in Fusion 360. The mechanical design should become the manufacturing source for:

- 3D printable chassis parts
- Jetson Orin Nano mounting
- Camera and ToF sensor mounts
- Battery and power electronics packaging
- Motor, wheel, suspension, and drivetrain interfaces
- Cable routing and service access
- Revision-controlled printable exports

> Figure needed: Fusion 360 full rover render.

## Electrical Design

Electrical design work is tracked under the KiCad project in [KiCad/Rover_main](KiCad/Rover_main). As the design matures, this section should include the main schematic, PCB renders, power tree, connector map, and wiring harness notes.

> Figures needed: electrical block diagram, PCB render, power distribution diagram.

## Bill of Materials

A BOM will be made available as the hardware design stabilizes. It should be split by build area so the project is easier to source, reproduce, and test.

| BOM Area | Planned Contents | Status |
| --- | --- | --- |
| Mechanical | Printed parts, fasteners, wheels, motors, bearings, inserts, chassis hardware. | Planned |
| Electrical | Jetson Orin Nano 8GB, microcontrollers, sensors, motor drivers, power electronics, connectors, wiring. | Planned |
| Testing | Bench power supply, multimeter, logic analyzer, USB serial tools, calibration fixtures, test cables. | Planned |
| Manufacturing | Filament/resin, heat-set inserts, crimp tools, soldering tools, adhesives, assembly fixtures. | Planned |

## Repository Layout

```text
AI-Rover/
  KiCad/
    Rover_main/              Main rover electronics project
  Rover/
    Bringup/
      ToF/                   VL53L5CX firmware, serial parser, heat map viewer
      DHT11/                 DHT11 firmware and documentation
    include/
    lib/
    test/
    platformio.ini           PlatformIO environments for bring-up targets
    README.md                Firmware bring-up overview
  README.md                  Project overview
  LICENSE
```

## Quick Start

The current runnable work is inside the `Rover/` PlatformIO project.

Build and upload the ToF bring-up firmware:

```powershell
cd Rover
pio run -e pico_tof -t upload
```

Run the ToF heat map viewer:

```powershell
python run_heatmap.py --port COM3
```

Build and upload the DHT11 bring-up firmware:

```powershell
cd Rover
pio run -e pico_dht11 -t upload
pio device monitor -b 115200
```

## Roadmap

| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| 1. Subsystem bring-up | Validate sensors, microcontroller firmware, serial tools, power assumptions, and electrical interfaces. | Each subsystem has wiring docs, test commands, and known-good output. |
| 2. Mechanical prototype | Create printable Fusion 360 rover assembly and mount real electronics/sensors. | Rover body can be printed, assembled, and serviced. |
| 3. Electrical integration | Move from bench wiring to integrated power, connectors, and PCB/harness design. | Electronics operate reliably from rover power. |
| 4. Mobility integration | Add drivetrain control, motor drivers, and basic safety behavior. | Rover can be manually commanded and stopped safely. |
| 5. Autonomy stack | Integrate Jetson perception, local LLM high-level control, and navigation software. | Rover can reason over goals and choose local actions. |
| 6. RL exploration | Introduce RL for low-level decision making after deterministic baselines exist. | Learned controller can be compared against classical control behavior. |

## Author

Devon Rice  
ricedevon3@gmail.com \
B.S. Aerospace Engineering Virginia Tech '26 \
M.S. Aerispace Engineering Virginia Tech '27