import argparse
import configparser as cp
import os
import random
from pathlib import Path

try:
    from termcolor import colored
except ImportError:  # pragma: no cover - fallback when termcolor isn't installed
    def colored(text, _color):
        return text
from .pokemons import pokemons
from .one_liners import one_liners

def main():
    parser = argparse.ArgumentParser(description = 'Display a Custom Message, a Pokemon ASCII Art and a Random Oneliner.\n'+colored('NOTE: Remember to turn off poketerm using -t 0 tag before you uninstall it','red'))
    parser.add_argument('-p','--pokemon',help='pokemon name for ASCII art. [noascii] for disabling ASCII art',choices=pokemons.keys())
    parser.add_argument('-l','--list',help='list available pokemons',action='store_true')
    parser.add_argument('-o','--one-liner',help='turn one liner on [1] or off [0]',type=int,choices=[0,1])
    parser.add_argument('-m','--message',help='custom message to be displayed in the start. [nomessage] for no message')
    #parser.add_argument('-a','--ascii', help='turn ASCII art on [1] or off [0]',type=int, choices = [0,1])
    parser.add_argument('-t','--turn-on',help='turn on poketerm [1], turn off [0]',type=int,choices=[0,1])
    parser.add_argument('-s','--show',help='run poketerm with the active configuration',action='store_true')

    args = parser.parse_args()
    '''
    print("INPUT ARGS")
    for arg in vars(args):
        print(arg,getattr(args,arg))
    print()'''
    curr_path = Path(__file__).resolve().parent
    default_config_path = curr_path / 'poketermconfig.ini'
    '''
    if os.path.exists(default_config_path):
        print("Found Config")
    else:
        print("Could not find config")
    '''

    default_config = cp.ConfigParser()
    default_config.read(default_config_path)

    config_dir = Path.home() / '.config' / 'poketerm'
    config_dir.mkdir(parents=True, exist_ok=True)
    local_config_path = config_dir / 'poketermconfig.ini'
    local_config = cp.ConfigParser()

    if local_config_path.exists():  # If local config file exists
        local_config.read(local_config_path)
        try:
            change_config(args, local_config_path)
        except Exception:
            with open(local_config_path, 'w') as configfile:
                default_config.write(configfile)
            try:
                change_config(args, local_config_path)
            except Exception:
                try:
                    local_config_path.unlink()
                except FileNotFoundError:
                    pass
                print("Unable to read local config, maybe try", colored(" $poketerm -t 1", "green"), "with sudo?")
            local_config.read(local_config_path)
    else:  # If local config file dne
        with open(local_config_path, 'w') as configfile:
            default_config.write(configfile)
        try:
            change_config(args, local_config_path)
        except Exception:
            try:
                local_config_path.unlink()
            except FileNotFoundError:
                pass
            print("Unable to read local config, maybe try", colored(" $poketerm -t 1", "green"), "with sudo?")
        local_config.read(local_config_path)

    if args.list:
        print("Available Pokemons are")
        for key in pokemons.keys():
            print(key)
            print(pokemons[key])

    if args.show:
        # show message
        msg = local_config["DEFAULTS"].get("message", "")
        if msg and msg.lower() != "none":
            print(msg)

        # show ascii art        
        if local_config["DEFAULTS"]["pokemon"] == "noascii":
            pass
        else:
            print(pokemons[local_config["DEFAULTS"]["pokemon"]])

        # show random one liner
        if local_config["DEFAULTS"]["one-liner"] == 'True':
            print(random.choice(one_liners))

def change_config(args,path):
    config = cp.ConfigParser()
    config.read(path)
    '''
    for section in config.sections():
        for (key,val) in config.items(section):
            print(key,val)
    '''
    if args.pokemon != None:
        config["DEFAULTS"]["pokemon"] = args.pokemon
    if args.message != None:
        if args.message == "nomessage":
            config["DEFAULTS"]["message"] = 'None'
        else:
            config["DEFAULTS"]["message"] = args.message
    if args.one_liner != None:
        if args.one_liner == 1:
            config["DEFAULTS"]["one-liner"] = 'True'
        else:
            config["DEFAULTS"]["one-liner"] = 'False'
    '''
    if args.ascii != None:
        if args.ascii == 1:
            config["DEFAULTS"]["ascii"] = 'True'
        else:
            config["DEFAULTS"]["ascii"] = 'False'
            '''
    def ensure_line(file_path: Path, line: str) -> None:
        if not file_path.exists():
            return
        with file_path.open('r+') as f:
            lines = [l.rstrip('\n') for l in f.readlines()]
            if line not in lines:
                f.write(line + '\n')

    def ensure_line_prepend(file_path: Path, line: str) -> None:
        """Ensure a line exists at the top of a file without duplicating it."""
        if not file_path.exists():
            return
        with file_path.open('r+') as f:
            lines = f.readlines()
            if any(l.rstrip('\n') == line for l in lines):
                return
            f.seek(0)
            f.write(line + '\n')
            f.writelines(lines)

    def remove_line(file_path: Path, line: str) -> None:
        if not file_path.exists():
            return
        with file_path.open('r') as f:
            lines = f.readlines()
        with file_path.open('w') as f:
            for existing in lines:
                if existing.rstrip('\n') != line:
                    f.write(existing)

    if args.turn_on is not None:
        bash_startup = "poketerm -s || echo reinstall poketerm and turn it off"
        p10k_quiet = "typeset -g POWERLEVEL9K_INSTANT_PROMPT=quiet"
        bash_files = ('.bashrc', '.bash_profile')
        zsh_files = ('.zshrc', '.zprofile')
        if args.turn_on == 1:
            config["DEFAULTS"]["poketerm"] = 'True'
            for fname in bash_files:
                ensure_line(Path.home() / fname, bash_startup)
            for fname in zsh_files:
                ensure_line_prepend(Path.home() / fname, p10k_quiet)
                ensure_line(Path.home() / fname, bash_startup)
        else:
            config["DEFAULTS"]["poketerm"] = 'False'
            for fname in bash_files:
                remove_line(Path.home() / fname, bash_startup)
            for fname in zsh_files:
                remove_line(Path.home() / fname, bash_startup)

    with open(path,'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    main()

