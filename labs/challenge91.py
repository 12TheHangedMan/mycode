#!/usr/bin/env python3

import requests
import random

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    
    print("let random help you pick")
    pokenum = random.randint(1,151)

    pokeapi= requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokenum}").json()
    
    #print(pokeapi)
    print(pokeapi["sprites"]["front_default"])
    
    #part2 done
    print("\nNow printing all moves of the pokemon")
    for i in pokeapi["moves"]:        
        print(i["move"]["name"])
   
    #part3
    print(f"\npokeapi{pokeapi['game_indices']}")
    #without looop    
    print(len(pokeapi["game_indices"]))

if __name__ =="__main__":
    main()

