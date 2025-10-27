#!/usr/bin/python3
"""a module that handles assignment operations"""


num = int(input("Enter any number of your choice: "))

num += 5
print("Addition assignment: {}".format(num))

num -= 3
print("Subtraction assignment: {}".format(num))

num *= 2
print("Multiplication assignment: {}".format(num))

num /= 2
print("Division assignment: {}".format(num))

num %= 3
print("Modulus assignment: {}".format(num))

num **= 2
print("Exponential assignment: {}".format(num))

num //= 2
print("Floor division assignment: {}".format(num))
