"""
Guesses what number (between 1-100) you are thinking of
"""

import random as r

lower_limit = 0
upper_limit = 100
guess = r.randint(lower_limit, upper_limit)

while True:
    inp = input(
        'Is the number {}?\n'
        'higher = h, lower = l, yes = y\n'.format(guess)
    )

    if inp == 'h':
        lower_limit = guess + 1

    elif inp == 'l':
        upper_limit = guess - 1

    elif inp == 'y':
        print('Ha! clever I am')
        break

    try:
        guess = r.randint(lower_limit, upper_limit)
    
    # if upper-lower = 0, it means the person has been lying somewhere
    # The correct number was already outputed by the computer
    except:
        print('Human is liar, I already guessed the correct number')
