#!/usr/bin/python3
"""a module that calculates the area of a rectangle"""


length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

if length <= 0 or width <= 0:
    print("Errror: length and width must be positive numbers")

area = length * width
print(f"length: {length}")
print(f"Width: {width}")
print(f"Area = {length} * {width} = {area}") 