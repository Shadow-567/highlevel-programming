#!/usr/bin/python3
"""a module that asks for password"""

correct_password = ("python123")
while True:
    password = input("Enter your password:")

    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again")