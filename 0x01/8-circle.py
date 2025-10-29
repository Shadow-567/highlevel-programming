#!/usr/bin/python3
"""a module that calculates the area of a circle"""


def circle(radius, PI):
    """
       A function that contains area of a triangle
       Args:
           radius: a value for the radius of the circle
           PI: a constant value for the PI of the circle
       Return:
           an area of circle 
    """
    return 3.142 * radius ** 2

if __name__ == "__main__":
    radius = int(input("Enter the radius of the circle: "))
    PI = 3.142
    area = circle(radius, PI)

    print(f"The area of the rectangle: {area}")