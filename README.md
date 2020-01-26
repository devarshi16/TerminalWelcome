# TerminalWelcome

Get greeted by custom message and/or

Pokemon ascii art and/or

A random one-liner when you switch your terminal on

![alt text](https://github.com/devarshi16/TerminalWelcome/blob/master/pika.png)

## Installation

```
$pip install poketerm
```

Turn on poketerm
```
$poketerm -t 1
```

Turn off poketerm
```
$poketerm -t 0
```

## Poketerm help
```
usage: main.py [-h] [-p {bulbasaur,dugtrio,meowth,pikachu,noascii}] [-l]
               [-o {0,1}] [-m MESSAGE] [-t {0,1}] [-s]

Display a Custom Message, a Pokemon ASCII Art and a Random Oneliner.
NOTE: Remember to turn off poketerm using -t 0 tag before you uninstall
it

optional arguments:
  -h, --help            show this help message and exit
  -p {bulbasaur,dugtrio,meowth,pikachu,noascii}, --pokemon {bulbasaur,dugtrio,meowth,pikachu,noascii}
                        pokemon name for ASCII art. [noascii] for disabling
                        ASCII art
  -l, --list            list available pokemons
  -o {0,1}, --one-liner {0,1}
                        turn one liner on [1] or off [0]
  -m MESSAGE, --message MESSAGE
                        custom message to be displayed in the start. [nomessage] for
                        no message
  -t {0,1}, --turn-onf {0,1}
                        turn on poke term [1], turn off [0]
  -s, --show            run poketerm with the active configuration
```


## Acknowledgments

Thanks to (http://silgro.com/fortunes.txt) for their one-liner database.
