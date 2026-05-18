# DHT11 Temperature and Humidity Bring-Up

This folder contains simple Raspberry Pi Pico firmware for reading a DHT11 temperature and humidity sensor on `GP10`.

## Wiring

| DHT11 Pin | Raspberry Pi Pico |
| --- | --- |
| VCC | 3V3 |
| DATA | GP10 |
| GND | GND |

Use a pull-up resistor from DATA to 3V3 if your DHT11 breakout board does not already include one.

## Firmware Layout

- `main_temp_humid.cpp` starts serial output and calls the sensor helper functions.
- `TempHumidSensor.cpp` owns DHT11 initialization, timing, reads, validation, and serial printing.
- `TempHumidSensor.h` exposes the helper functions used by `main_temp_humid.cpp`.

## Build and Upload

```powershell
pio run -e pico_dht11 -t upload
pio device monitor -b 115200
```
