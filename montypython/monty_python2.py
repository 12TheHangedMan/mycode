#!/usr/bin/env python3

round = 0

while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input("Your guess-->")

    if answer == 'Brian':
        print('correct')
        break
    elif round == 3:
        print("sry, the answer was Brian. And you didn't make it in 3 guesses")
        break
    else:
        print("sorry! Try again")
       
