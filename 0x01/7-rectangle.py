#!/usr/bin/python3
"""a module that calculates the area of a rectangle"""


def rectangle(length, width):
    """
       A function that contains area of a rectangle
       Args:
           length: a value for the length of the rectangle
           width: a value for the width of the rectangle
       Return:
           an area of a rectangle
    """
    return length * width

if __name__ == "__main__":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = rectangle(length, width)

    print(f"The area of the rectangle: {area}")