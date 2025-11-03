#!/usr/bin/python3
"""a module that performs a guessing game"""

import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the number guessing game")
print("I'am thinking of a number between 1 and 100")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations, you guessed it in {attempts} attempts")
        break

    if guess < secret_number:
        print("Too low, try a higher number")
    
    else:
        print("Too high, guess a lower number")