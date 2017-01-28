"""
Guesses what number (between 1-100) you are thinking of
"""

import random as r

correct = False
guess = r.randint(0, 100)
guessLowerLimit = 0
guessUpperLimit = 100

while True:
    print(guess)
    inp = input("lower or higher or correct? ")
    if inp == 'lower':
        guessUpperLimit = guess - 1
        guess = r.randint(guessLowerLimit, guessUpperLimit)

    elif inp == 'higher':
        guessLowerLimit = guess + 1
        guess = r.randint(guessLowerLimit, guessUpperLimit)

    elif inp == 'correct':
        print("Ha, my guess was correct")
        break
