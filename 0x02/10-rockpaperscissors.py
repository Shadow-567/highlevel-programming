#!/usr/bin/python3
"""a implements a game of chance"""

import random

def play():
    print("Welcome to rock, paper, scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") \
            or (user_choice == "paper" and computer_choice == "rock") \
            or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == "__main__":
    play()    