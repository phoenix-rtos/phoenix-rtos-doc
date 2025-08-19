#!/usr/bin/env python3

import argparse
import shlex
import shutil
import sys
from pathlib import Path
from subprocess import check_call

REPO_DIR = Path(__file__).resolve().parent
VENV_DIR = REPO_DIR / "_venv"

parser = argparse.ArgumentParser()

parser.add_argument(
    "--dry",
    action="store_true",
    help="print commands that would be run without executing",
)
parser.add_argument(
    "--force",
    action="store_true",
    help="remove old virtual environment if exists",
)


cmd_args = parser.parse_args()


def error(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def call(cmd, *args, **kwargs):
    str_cmd = " ".join(shlex.quote(str(x)) for x in cmd)
    print(f"Running command: {str_cmd}")
    if not cmd_args.dry:
        check_call(cmd, *args, **kwargs)


def install_requirements(requirements_path):
    print(f"Installing requirements from {requirements_path}")
    call([*pip_install, "-r", requirements_path])


if VENV_DIR.exists():
    if not cmd_args.force:
        error(
            f"ERROR: virtual environment directory already exists: {VENV_DIR.absolute()}\n"
            f"Add '--force' flag to remove it before create new one"
        )

    print(f"deleting old virtual environment: {VENV_DIR}")
    if cmd_args.dry:
        print(f"Running command: rm -rf {VENV_DIR}")
    else:
        shutil.rmtree(VENV_DIR)

print(f"Creating new virtual environment: {VENV_DIR}")
call(["python3", "-m", "venv", VENV_DIR], cwd=REPO_DIR)

pip_install = [VENV_DIR / "bin" / "python3", "-m", "pip", "install"]
install_requirements(REPO_DIR / "requirements.txt")

print("Virtual environment created")
print(f"To enter run: source {VENV_DIR}/bin/activate")
