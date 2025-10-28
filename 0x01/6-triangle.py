#!/usr/bin/python3
"""a module that calculates the area of a traingle"""


base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triange: "))

if base <= 0 or height <= 0:
    print("Errror: Base and height must be positive numbers")
area = 0.5 * base * height
print(f"Base: {base}")
print(f"Height: {height}")
print(f"Area = 0.5 * {base} * {height} = {area}")