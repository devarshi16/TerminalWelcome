import configparser as cp
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def run_cli(args: list[str], env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "src.main", *args],
        capture_output=True,
        text=True,
        env=env,
    )


def test_runs_counter_increment() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        result = run_cli(["-p", "noascii", "-o", "0", "-s"], env=env)
        assert result.returncode == 0
        config_path = Path(tmp_home) / ".config" / "poketerm" / "poketermconfig.ini"
        parser = cp.ConfigParser()
        parser.read(config_path)
        assert parser["DEFAULTS"].getint("runs") == 1


def test_donation_message_after_threshold() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        config_dir = Path(tmp_home) / ".config" / "poketerm"
        config_dir.mkdir(parents=True)
        config_path = config_dir / "poketermconfig.ini"
        config_path.write_text(
            "[DEFAULTS]\n"
            "pokemon = pikachu\n"
            "one-liner = False\n"
            "message = None\n"
            "poketerm = True\n"
            "ascii = True\n"
            "dialog = False\n"
            "runs = 10000\n"
            "sponsor_reminders = 0\n"
        )
        result = run_cli(["-p", "noascii", "-o", "0", "-s"], env=env)
        assert result.returncode == 0
        out = result.stdout.lower()
        assert "sponsoring" in out
        assert "only" in out and "three times" in out
        assert "https://github.com/sponsors/devarshi16" in result.stdout
        parser = cp.ConfigParser()
        parser.read(config_path)
        defaults = parser["DEFAULTS"]
        assert defaults.getint("runs") == 10001
        assert defaults.getint("sponsor_reminders") == 1


def test_donation_message_shows_only_thrice() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        config_dir = Path(tmp_home) / ".config" / "poketerm"
        config_dir.mkdir(parents=True)
        config_path = config_dir / "poketermconfig.ini"
        config_path.write_text(
            "[DEFAULTS]\n"
            "pokemon = pikachu\n"
            "one-liner = False\n"
            "message = None\n"
            "poketerm = True\n"
            "ascii = True\n"
            "dialog = False\n"
            "runs = 10002\n"
            "sponsor_reminders = 2\n"
        )
        # Third reminder should be shown
        result = run_cli(["-p", "noascii", "-o", "0", "-s"], env=env)
        assert result.returncode == 0
        assert "sponsor" in result.stdout.lower()
        assert "https://github.com/sponsors/devarshi16" in result.stdout
        parser = cp.ConfigParser()
        parser.read(config_path)
        defaults = parser["DEFAULTS"]
        assert defaults.getint("runs") == 10003
        assert defaults.getint("sponsor_reminders") == 3

        # Fourth run should not show reminder
        result = run_cli(["-p", "noascii", "-o", "0", "-s"], env=env)
        assert result.returncode == 0
        assert "sponsor" not in result.stdout.lower()
        parser.read(config_path)
        defaults = parser["DEFAULTS"]
        assert defaults.getint("runs") == 10004
        assert defaults.getint("sponsor_reminders") == 3

