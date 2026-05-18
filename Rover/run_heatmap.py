import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
TOF_LAUNCHER = PROJECT_ROOT / "Bringup" / "ToF" / "run_heatmap.py"


def main() -> int:
    command = [sys.executable, str(TOF_LAUNCHER), *sys.argv[1:]]
    return subprocess.call(command, cwd=PROJECT_ROOT)


if __name__ == "__main__":
    sys.exit(main())
