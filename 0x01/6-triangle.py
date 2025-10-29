#!/usr/bin/python3
"""a module that calculates the area of a traingle"""

def triangle(base, height):
    """
       A function that contains area of a triangle
       Args:
           base: a value for the base of the triangle
           height: a value for the height of the triangle
       Return:
           an area of a triangle 
    """
    return 0.5 * base * height

if __name__ == "__main__":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triange: "))
    area = triangle(base, height)

    print(f"The area of the triangle: {area}")