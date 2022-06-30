import subprocess
import sys

from numcertain import __version__


def test_cli_version_shows_version():
    cmd = [sys.executable, "-m", "numcertain", "--version"]
    assert __version__ == subprocess.check_output(cmd).decode().strip()


def test_cli_help_shows_help():
    cmd = [sys.executable, "-m", "numcertain", "--help"]
    assert (
        subprocess.check_output(cmd)
        .decode()
        .strip()
        .startswith("Usage: python -m numcertain")
    )


def test_cli_noargs_shows_help():
    cmd = [sys.executable, "-m", "numcertain"]
    assert (
        subprocess.check_output(cmd)
        .decode()
        .strip()
        .startswith("Usage: python -m numcertain")
    )
