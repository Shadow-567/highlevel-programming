#!/usr/bin/python3
"""a module that implement fizzbuzz number using loop"""


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")