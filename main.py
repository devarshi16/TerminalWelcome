import argparse
import pokemons
from config.poke_config import config

def main():
    parser = argparse.ArgumentParser(description = 'Display a Custom Message, a Pokemon ASCII Art and a Random Oneliner')
    parser.add_argument('-p','--pokemon',help='pokemon name for ASCII art. 0 for disabling ASCII art')
    parser.add_argument('-l','--list',help='list available pokemons. 0 for only names, 1 displays arts aswell',type=int,choices=[1,0])
    parser.add_argument('-o','--one-liner',help='turn one liner on[1] or off[0]',type=int,choices=[0,1]) 
    parser.add_argument('-m','--message',help='custom message to be displayed in the start. [0] for no message')

    args = parser.parse_args()
    print(args.pokemon)
    
    '''
def change_config(pokemon=config["pokemon"],one_liner=config["one-liner"],message=config["message"]):
    with open('`
    '''
main()
