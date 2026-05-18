# AI Rover

AI Rover is an embedded robotics project focused on building up the software stack for a small autonomous rover. The current repository contains early bring-up work for the rover platform, starting with a Raspberry Pi Pico, a VL53L5CX time-of-flight sensor used for short-range depth sensing, and a DHT11 temperature/humidity sensor used for basic environmental readings.

The first software milestone is a working ToF sensor bring-up path: firmware reads an 8x8 distance grid from the sensor, streams the data over USB serial, and a Python utility displays the readings as a live heat map. The DHT11 bring-up follows the same pattern with simple firmware that streams temperature and humidity over USB serial. Together, these create a foundation for later perception, obstacle awareness, environmental monitoring, navigation, and autonomy features.

## Project Background

This project is being developed as a practical robotics and embedded systems platform. The goal is to incrementally bring up each hardware subsystem, verify it in isolation, and then integrate those pieces into a rover capable of sensing, decision-making, and motion control.

Current focus areas:

- Raspberry Pi Pico firmware development with PlatformIO
- VL53L5CX time-of-flight sensor integration
- DHT11 temperature/humidity sensor integration
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
      ToF_Bringup_Guide.md
      serial_heatmap.py
      run_heatmap.py
      run_heatmap.bat
      requirements.txt
    DHT11/
      main_temp_humid.cpp
      TempHumidSensor.cpp
      TempHumidSensor.h
      README.md
  include/
  lib/
  test/
  platformio.ini
  run_heatmap.py
```

## Hardware Bring-Up

The bring-up firmware lives under `Bringup/`, with separate PlatformIO environments for each sensor target.

### ToF Sensor

- Raspberry Pi Pico
- VL53L5CX time-of-flight sensor
- I2C connection on Pico `GP0` / `GP1`
- USB serial monitor at `115200` baud

For wiring, setup, and heat map usage, see [Bringup/ToF/ToF_Bringup_Guide.md](Bringup/ToF/ToF_Bringup_Guide.md).

Build and upload the ToF firmware with:

```powershell
pio run -e pico_tof -t upload
```

### DHT11 Temperature/Humidity Sensor

- Raspberry Pi Pico
- DHT11 temperature and humidity sensor
- Data connection on Pico `GP10`
- USB serial monitor at `115200` baud

For wiring and firmware notes, see [Bringup/DHT11/README.md](Bringup/DHT11/README.md).

Build and upload the DHT11 firmware with:

```powershell
pio run -e pico_dht11 -t upload
pio device monitor -b 115200
```

## Getting Started

1. Install PlatformIO.
2. Connect the sensor you want to test to the Raspberry Pi Pico as described in its bring-up guide.
3. Build and upload the matching PlatformIO environment:

```powershell
pio run -e pico_tof -t upload
pio run -e pico_dht11 -t upload
```

4. For the ToF heat map utility, install the Python dependencies:

```powershell
pip install -r Bringup/ToF/requirements.txt
```

5. Run the ToF heat map viewer:

```powershell
python run_heatmap.py
```

## Author

Devon Rice  
ricedevon3@gmail.com
