import argparse
import sys
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import serial
from serial.tools import list_ports


GRID_SIZE = 8
FRAME_MARKER = "Distance Grid (mm):"
PICO_PORT_KEYWORDS = ("pico", "rp2040", "raspberry pi")


def find_serial_port() -> Optional[str]:
    ports = list(list_ports.comports())

    if len(ports) == 1:
        return ports[0].device

    pico_ports = [
        port
        for port in ports
        if any(
            keyword in f"{port.description} {port.manufacturer}".lower()
            for keyword in PICO_PORT_KEYWORDS
        )
    ]

    if len(pico_ports) == 1:
        return pico_ports[0].device

    return None


def read_distance_frame(serial_port: serial.Serial) -> np.ndarray:
    rows: List[List[int]] = []

    while True:
        line = serial_port.readline().decode("utf-8", errors="ignore").strip()
        if line == FRAME_MARKER:
            break

    while len(rows) < GRID_SIZE:
        line = serial_port.readline().decode("utf-8", errors="ignore").strip()

        if not line or line.startswith("-"):
            continue

        values = [int(value) for value in line.split()]

        if len(values) == GRID_SIZE:
            rows.append(values)

    return np.array(rows)


def plot_serial_heatmap(port: str, baud: int) -> None:
    with serial.Serial(port, baud, timeout=2) as serial_port:
        print(f"Reading serial data from {port} at {baud} baud...")

        first_frame = read_distance_frame(serial_port)

        plt.ion()
        figure, axis = plt.subplots()
        heatmap = axis.imshow(first_frame, cmap="inferno", interpolation="nearest")
        colorbar = figure.colorbar(heatmap, ax=axis)
        colorbar.set_label("Distance (mm)")

        axis.set_title("VL53L5CX Distance Heat Map")
        axis.set_xlabel("X Zone")
        axis.set_ylabel("Y Zone")

        while plt.fignum_exists(figure.number):
            frame = read_distance_frame(serial_port)
            heatmap.set_data(frame)
            heatmap.set_clim(vmin=np.min(frame), vmax=np.max(frame))
            figure.canvas.draw_idle()
            plt.pause(0.001)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read the Rover serial distance grid and display it as a live heat map."
    )
    parser.add_argument(
        "--port",
        help="Serial port for the Pico, such as COM3. If omitted, the script uses the only detected serial port.",
    )
    parser.add_argument(
        "--baud",
        type=int,
        default=115200,
        help="Serial baud rate. Default: 115200.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    port = args.port or find_serial_port()

    if port is None:
        print("Could not choose a serial port automatically.")
        print("Run with --port COMx, for example: python run_heatmap.py --port COM3")
        print()
        print("Detected ports:")
        detected_ports = list(list_ports.comports())
        if not detected_ports:
            print("  None")
        for detected_port in detected_ports:
            print(
                f"  {detected_port.device}: "
                f"{detected_port.description} "
                f"({detected_port.manufacturer or 'unknown manufacturer'})"
            )
        return 1

    try:
        plot_serial_heatmap(port, args.baud)
    except serial.SerialException as error:
        print(f"Serial error: {error}")
        return 1
    except KeyboardInterrupt:
        print("Stopped.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
