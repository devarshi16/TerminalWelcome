#!usr/bin/env python
import os
from one_liners import one_liners
from poke_config import config
from pokemons import pokemons
import random

def display_one_liner():
    if config["one-liner"]:
        print(random.choice(one_liners))

def display_ascii_art():
    print(pokemons[config["pokemon"]])

def display_message():
    if config["message"] == None:
        return
    else:
        print(config["message"])

display_message()
display_ascii_art()
display_one_liner()

