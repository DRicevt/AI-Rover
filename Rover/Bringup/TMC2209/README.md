# TMC2209 NEMA 17 Stepper Bring-Up

This folder contains simple Raspberry Pi Pico firmware for driving a TMC2209 stepper driver with a NEMA 17 stepper motor in STEP/DIR mode.

## Wiring

| TMC2209 Pin | Raspberry Pi Pico |
| --- | --- |
| DIR | GP6 |
| STEP | GP7 |
| EN | GP8 |
| GND | GND |
| VM | Motor power supply positive |
| GND / PGND | Motor power supply ground |

## Motor Wiring

| Motor Wire | TMC2209 Terminal |
| --- | --- |
| Black | 1A |
| Green | 2A |
| Blue | 1B |
| Red | 2B |

`EN` is active-low on typical TMC2209 modules, so the firmware drives `GP8` low to enable the driver.

## Firmware Behavior

- `main_tmc2209.cpp` starts serial output and calls the motor helper functions.
- `StepperMotor.cpp` owns GPIO setup, enable control, step pulse generation, and periodic direction changes.
- The motor direction toggles every 3 seconds.
- Step pulses are generated every 700 microseconds, which produces a moderate bring-up speed.

## Build and Upload

```powershell
pio run -e pico_tmc2209 -t upload
pio device monitor -b 115200
```
