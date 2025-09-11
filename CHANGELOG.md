# Changelog

All notable changes to this project will be documented in this file.

## [0.10.2] - 2025-09-09
### Added
- Track the number of times poketerm is run and remind heavy users to donate.

## [0.10.1] - 2025-09-09
### Added
- Install poketerm into zsh startup files alongside bash equivalents.
### Fixed
- Avoid creating shell startup files for shells that are not present.
- Silence Powerlevel10k instant prompt warning by setting
  `POWERLEVEL9K_INSTANT_PROMPT=quiet` when adding to zsh configs and
  placing the variable at the top of zsh startup files to prevent
  warnings.
- Skip adding a second `POWERLEVEL9K_INSTANT_PROMPT` line if one already
  exists in zsh startup files.

## [0.10.0] - 2025-09-08
### Changed
- Fix CLI flag typo and streamline message handling.
- Replace fragile shell edits with Python file I/O and use XDG config directory.
- Harden startup scripts to copy `fortunes.txt` only when missing and safely quote paths.
- Drop Python 2 support, add `pyproject.toml`, and require Python 3.7+.
- Add basic CLI test to ensure interface stability.

