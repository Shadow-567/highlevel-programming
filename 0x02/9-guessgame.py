#!/usr/bin/python3
"""a module that imolements a guess game"""

import random

trials = 3

while trials > 0:
    num = random.randint(1, 5)
    guess = int(input("Guess a number between 1 and 5: "))
    if guess == num:
        print("Congratulations you just won yourself $1000: ")
        break
    else:
        print("Try again, you guessed wrong: ")
    trials -= 1