#!/usr/bin/pyhon3
"""a module taht handles conditonal statement"""


age = int(input("Enter your age: "))

if age >= 10 and age <= 17:
    print("You're a teenager")
elif age >= 18 and age <= 40:
    print("You're an adult")
else:
    print("You're a senior citizen")