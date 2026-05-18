# AI Rover

AI Rover is an embedded robotics project focused on building up the software stack for a small autonomous rover. The current repository contains the early bring-up work for the rover platform, starting with a Raspberry Pi Pico and a VL53L5CX time-of-flight sensor used for short-range depth sensing.

The first software milestone is a working ToF sensor bring-up path: firmware reads an 8x8 distance grid from the sensor, streams the data over USB serial, and a Python utility displays the readings as a live heat map. This creates a foundation for later perception, obstacle awareness, navigation, and autonomy features.

## Project Background

This project is being developed as a practical robotics and embedded systems platform. The goal is to incrementally bring up each hardware subsystem, verify it in isolation, and then integrate those pieces into a rover capable of sensing, decision-making, and motion control.

Current focus areas:

- Raspberry Pi Pico firmware development with PlatformIO
- VL53L5CX time-of-flight sensor integration
- Serial telemetry from embedded firmware to host tools
- Python-based visualization for sensor debugging
- Clean bring-up documentation for repeatable hardware testing

## Repository Layout

```text
Rover/
  Bringup/
    ToF/
      main_ToF.cpp
      RoverSensor.cpp
      RoverSensor.h
      serial_heatmap.py
      run_heatmap.py
      run_heatmap.bat
      requirements.txt
    ToF_Bringup_Guide.md
  include/
  lib/
  test/
  platformio.ini
  run_heatmap.py
```

## Hardware Bring-Up

The active firmware target is the ToF bring-up under `Bringup/ToF`. It is configured in `platformio.ini` as the PlatformIO source directory.

Primary hardware:

- Raspberry Pi Pico
- VL53L5CX time-of-flight sensor
- I2C connection on Pico `GP0` / `GP1`
- USB serial monitor at `115200` baud

For wiring, setup, and heat map usage, see [Bringup/ToF_Bringup_Guide.md](Bringup/ToF_Bringup_Guide.md).

## Getting Started

1. Install PlatformIO.
2. Connect the VL53L5CX sensor to the Raspberry Pi Pico as described in the bring-up guide.
3. Build and upload the Pico firmware from this project.
4. Install the Python dependencies for the heat map utility:

```powershell
pip install -r Bringup/ToF/requirements.txt
```

5. Run the heat map viewer:

```powershell
python run_heatmap.py
```

## Author

Devon Rice  
ricedevon3@gmail.com
