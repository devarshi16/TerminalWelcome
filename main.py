import argparse
import pokemons
import configparser as cp
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description = 'Display a Custom Message, a Pokemon ASCII Art and a Random Oneliner.\n'+colored('NOTE: Remember to turn off poketerm using -s 0 tag before you uninstall it','red'))
    parser.add_argument('-p','--pokemon',help='pokemon name for ASCII art. 0 for disabling ASCII art')
    parser.add_argument('-l','--list',help='list available pokemons',action='store_true')
    parser.add_argument('-o','--one-liner',help='turn one liner on[1] or off[0]',type=int,choices=[0,1]) 
    parser.add_argument('-m','--message',help='custom message to be displayed in the start. [0] for no message')
    parser.add_argument('-t','--turn-on',help='turn on poke term[1], turn off [0]',type=int,choices=[0,1])
    parser.add_argument('-s','--show',help='run poketerm with the active configuration',action='store_true')

    args = parser.parse_args()
    print(args.pokemon)
    for arg in vars(args):
        print(arg,getattr(args,arg))
    config
    '''
def change_config(config,pokemon=config['DEFAULTS']["pokemon"],one_liner=config['DEFAULTS']["one-liner"],message=config['DEFAULTS']["message"]):
    
    '''
def change_config(config,args):
    
main()
