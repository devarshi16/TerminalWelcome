import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.one_liners import one_liners
from src.pokemons import pokemons


def run_cli(args: list[str], env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "src.main", *args],
        capture_output=True,
        text=True,
        env=env,
    )


def test_help_runs() -> None:
    result = run_cli(["-h"])
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()


def test_show_pokemon() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        result = run_cli(["-o", "0", "-s"], env=env)
        assert result.returncode == 0
        assert pokemons["pikachu"] in result.stdout


def test_show_one_liner() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        result = run_cli(["-p", "noascii", "-s"], env=env)
        assert result.returncode == 0
        line = result.stdout.strip()
        assert line in one_liners


def test_change_default_pokemon() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        assert run_cli(["-p", "meowth"], env=env).returncode == 0
        result = run_cli(["-o", "0", "-s"], env=env)
        assert pokemons["meowth"] in result.stdout


def test_dialog_cloud() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        result = run_cli(["-p", "noascii", "-d", "1", "-s"], env=env)
        assert result.returncode == 0
        lines = result.stdout.splitlines()
        # bubble has 5 lines; second line contains the text
        assert len(lines) == 5
        inner = lines[1][2:-2]
        assert inner in one_liners


def test_turn_on_updates_zshrc() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        zshrc = Path(tmp_home) / ".zshrc"
        zshrc.write_text("export PATH=/usr/bin\n")
        assert run_cli(["-t", "1"], env=env).returncode == 0
        expected = (
            "typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet\n"
            "export PATH=/usr/bin\n"
            "poketerm -s || echo reinstall poketerm and turn it off\n"
        )
        assert zshrc.read_text() == expected
        assert run_cli(["-t", "0"], env=env).returncode == 0
        # The Powerlevel10k line remains at the top
        assert zshrc.read_text() == (
            "typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet\n"
            "export PATH=/usr/bin\n"
        )


def test_turn_on_does_not_duplicate_existing_p10k_line() -> None:
    with tempfile.TemporaryDirectory() as tmp_home:
        env = {**os.environ, "HOME": tmp_home}
        zshrc = Path(tmp_home) / ".zshrc"
        zshrc.write_text(
            "typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet\n"
            "alias ll='ls -al'\n"
        )
        assert run_cli(["-t", "1"], env=env).returncode == 0
        expected = (
            "typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet\n"
            "alias ll='ls -al'\n"
            "poketerm -s || echo reinstall poketerm and turn it off\n"
        )
        assert zshrc.read_text() == expected

