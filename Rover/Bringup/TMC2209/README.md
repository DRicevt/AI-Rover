# TMC2209 NEMA 17 Stepper Bring-Up

This folder contains simple Raspberry Pi Pico firmware for driving a TMC2209 stepper driver with a NEMA 17 stepper motor in STEP/DIR mode. It is the bench bring-up path for the rover drivetrain driver blocks before they are folded into the main rover control firmware.

The integrated rover schematic currently uses four TMC2209 SilentStepStick-style driver modules. Each module has dedicated `STEP`, `DIR`, and active-low `EN` signals, motor coil outputs routed to JST-XH motor connectors, local 3.3 V decoupling, and a 470 uF bulk capacitor on the motor supply rail.

Main schematic: [KiCad/Rover_main/Rover_main.svg](../../../KiCad/Rover_main/Rover_main.svg)

## Wiring

This single-driver wiring matches the standalone bring-up firmware:

| TMC2209 Pin | Raspberry Pi Pico |
| --- | --- |
| DIR | GP6 |
| STEP | GP7 |
| EN | GP8 |
| GND | GND |
| VM | Motor power supply positive |
| GND / PGND | Motor power supply ground |

The main rover schematic expands this pattern to four drivers:

| Driver | Enable | Step | Direction | UART |
| --- | --- | --- | --- | --- |
| STP_Driver_1 | `DRV1_EN` | `DRV1_STEP` | `DRV1_DIR` | `UART_DRV_1_2` |
| STP_Driver_2 | `DRV2_EN` | `DRV2_STEP` | `DRV2_DIR` | `UART_DRV_1_2` |
| STP_Driver_3 | `DRV3_EN` | `DRV3_STEP` | `DRV3_DIR` | `UART_DRV_3_4` |
| STP_Driver_4 | `DRV4_EN` | `DRV4_STEP` | `DRV4_DIR` | `UART_DRV_3_4` |

## Motor Wiring

| Motor Wire | TMC2209 Terminal |
| --- | --- |
| Black | 1A |
| Green | 2A |
| Blue | 1B |
| Red | 2B |

The KiCad schematic labels the same coil colors at each motor connector: black, green, blue, and red for motors 1 through 4.

`EN` is active-low on typical TMC2209 modules, so the firmware drives `GP8` low to enable the driver.

## Power Notes

- Provide motor power on `VM` from the rover motor supply, not from the Pico USB or 3.3 V rail.
- Tie Pico ground, driver logic ground, and motor supply ground together.
- Keep the driver bulk capacitor close to the driver module in the final wiring or PCB layout.
- Confirm the motor current limit on each TMC2209 module before connecting the motor.
- Power down before changing motor wiring or driver module jumpers.

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

## Author

Devon Rice  
ricedevon3@gmail.com \
B.S. Aerospace Engineering Virginia Tech '26 \
M.S. Aerospace Engineering Virginia Tech '27
