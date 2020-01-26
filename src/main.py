from __future__ import print_function
import argparse
from pokemons import pokemons
from one_liners import one_liners
import configparser as cp
from termcolor import colored
import random
import os

def main():
    parser = argparse.ArgumentParser(description = 'Display a Custom Message, a Pokemon ASCII Art and a Random Oneliner.\n'+colored('NOTE: Remember to turn off poketerm using -t 0 tag before you uninstall it','red'))
    parser.add_argument('-p','--pokemon',help='pokemon name for ASCII art. [noascii] for disabling ASCII art',choices=pokemons.keys())
    parser.add_argument('-l','--list',help='list available pokemons',action='store_true')
    parser.add_argument('-o','--one-liner',help='turn one liner on [1] or off [0]',type=int,choices=[0,1]) 
    parser.add_argument('-m','--message',help='custom message to be displayed in the start. [nomessage] for no message')
    #parser.add_argument('-a','--ascii', help='turn ASCII art on [1] or off [0]',type=int, choices = [0,1])
    parser.add_argument('-t','--turn-onf',help='turn on poke term [1], turn off [0]',type=int,choices=[0,1])
    parser.add_argument('-s','--show',help='run poketerm with the active configuration',action='store_true')

    args = parser.parse_args()
    '''
    print("INPUT ARGS")
    for arg in vars(args):
        print(arg,getattr(args,arg))
    print()'''
    curr_path = os.path.dirname(os.path.abspath(__file__))
    default_config_path = os.path.join(curr_path,'poketermconfig.ini')
    '''
    if os.path.exists(default_config_path):
        print("Found Config")
    else:
        print("Could not find config")
    '''

    default_config = cp.ConfigParser()
    default_config.read(default_config_path)

    local_config_path = os.path.join(os.environ["HOME"],'poketermconfig.ini')
    local_config = cp.ConfigParser()

    if os.path.exists(local_config_path): # If local config file exists
        local_config.read(local_config_path)
        try:
            change_config(args,local_config_path)
        except:
            with open(local_config_path,'w') as configfile:
                default_config.write(configfile)
            change_config(args,local_config_path)
            local_config.read(local_config_path)
    else: # If local config file dne
        with open(local_config_path,'w') as configfile:
            default_config.write(configfile)
        change_config(args,local_config_path)
        local_config.read(local_config_path)

    if args.list:
        print("Available Pokemons are")
        for key in pokemons.keys():
            print(key)
            print(pokemons[key])

    if args.show:
        # show message
        if local_config["DEFAULTS"]["message"] == None or local_config["DEFAULTS"]["message"] == "none" or local_config["DEFAULTS"]["message"]=="None":
            pass
        else:
            print(local_config["DEFAULTS"]["message"])

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
    if args.turn_onf != None:
        if args.turn_onf == 1:
            config["DEFAULTS"]["poketerm"] = 'True'
            os.system("""echo 'poketerm -s || echo reinstall poketerm and turn it off' >> ~/.bashrc""") 
        else:
            config["DEFAULTS"]["poketerm"] = 'False'
            os.system("""sed -i '/poketerm -s || echo reinstall poketerm and turn it off/d' ~/.bashrc""")

    with open(path,'w') as configfile:
            config.write(configfile)
#main()
