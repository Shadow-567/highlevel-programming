#!/usr/bin/python3
"""a module that handles password check"""

password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit")
else:
    print("Password is valid")