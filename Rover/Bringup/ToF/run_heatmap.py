import subprocess
import sys
from pathlib import Path


BRINGUP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BRINGUP_DIR.parents[1]
VENV_PYTHON = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
REQUIREMENTS_FILE = BRINGUP_DIR / "requirements.txt"
HEATMAP_SCRIPT = BRINGUP_DIR / "serial_heatmap.py"


def get_python_executable() -> Path:
    if VENV_PYTHON.exists():
        return VENV_PYTHON

    return Path(sys.executable)


def install_requirements(python_executable: Path) -> None:
    subprocess.check_call(
        [
            str(python_executable),
            "-m",
            "pip",
            "install",
            "-r",
            str(REQUIREMENTS_FILE),
        ],
        cwd=PROJECT_ROOT,
    )


def run_heatmap(python_executable: Path) -> int:
    command = [str(python_executable), str(HEATMAP_SCRIPT), *sys.argv[1:]]
    return subprocess.call(command, cwd=BRINGUP_DIR)


def main() -> int:
    python_executable = get_python_executable()

    print(f"Using Python: {python_executable}")
    install_requirements(python_executable)

    print("Starting serial heat map...")
    return run_heatmap(python_executable)


if __name__ == "__main__":
    sys.exit(main())
