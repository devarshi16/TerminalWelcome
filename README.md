# TerminalWelcome
[![Downloads](https://pepy.tech/badge/poketerm)](https://pepy.tech/project/poketerm)
[![Downloads](https://pepy.tech/badge/poketerm/month)](https://pepy.tech/project/poketerm/month)
[![Downloads](https://pepy.tech/badge/poketerm/week)](https://pepy.tech/project/poketerm/week)

Get greeted by custom message and/or

Pokemon ascii art and/or

A random one-liner when you switch your terminal on

![alt text](https://github.com/devarshi16/TerminalWelcome/blob/master/poke.png)

## Installation

```
$ sudo pip install poketerm
```
**NOTE:** You need sudo permission for the package to work

Turn on poketerm
```
$poketerm -t 1
```

Turn off poketerm
```
$poketerm -t 0
```

**NOTE:** make sure to turn off poketerm before you uninstall it!

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

## List of available pokemons
```
$ poketerm -l
Available Pokemons are
pikachu

|\_                  _ 
 \ \               _/_|
  \ \_          __/ /
   \  \________/   /
    |              |
    /              |
   |   0       0   |
   |       _       |
   |()    __    () |
    \    (__)      |
bulbasaur
 
            ____M___
           (  /   \ \
     \ ----/\ (    ) )
     / O  O  |---- _/
    |   _         \
     \__U____/ _(  |
      |_/   |_/  |_/
dugtrio

              _______
             /       \
            |  0   0  |
          __|__  <>   | 
         /     \    __|__
        |       |  /     \
        | 0  0  | / 0  0  |
        |  <>   |/   <>   /
        |       |        /
       0oOwwwWwwOOoowwwwww
meowth

                ___                       ___ 
               |   \_    ^        ^     _/   |
               |     \_ | |      | |  _/ __  |
               |       \| | /""\ | | / _/  | |
               |    __..|"||____||"|../.  /  |
         __     \_ /    | ||____|| |    \/ _/    __ 
         \ """--__:      v  \../  v      :__--""" / 
          ""--___/     ____       ____    \___--""
                .     (_||_)     (_||_)    .
        ________|_                        __|_______
        \__________                       _________/
                .        __________        .
                  .      \   __   /      .
                    .     \_/__\_/     .
                      .              .
                        "..........."
noascii
```

## Change Pokemon ASCII art
```
$ poketerm -p meowth
```

## Change Custom Message
```
$ poketerm -m "Your Message Here"
```

## Turn off Random One-Liner
```
$ poketerm -o 0
```

## Turn off pokemon ascii art
```
$ poketerm -p noascii
```

## Turn off Custom Message
```
$ poketerm -m nomessage
```

## Acknowledgments

Thanks to (http://silgro.com/fortunes.txt) for their one-liner database.
