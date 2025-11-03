#!/usr/bin/python3
"""a module that solves equations on multiplication"""

num = int(input("Enter any number: "))
print(f"Multiplication table of {num}:")

for i in range(1, 11):
    result = num * i
    print(f" {num} * {i} = {result}")