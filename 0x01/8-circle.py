#!/usr/bin/python3
"""a module that calculates the area of a circle"""


radius = int(input("Enter the radius of the circle: "))
PI = 3.142

area = PI * radius ** 2
print(f"Radius: {radius}")
print(f"Area = {PI} * {radius} ** 2 = {area}")