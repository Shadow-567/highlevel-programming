#!/usr/bin/python3
"""a module that converts uppercase to lower case"""

def lower(str):
    """
    A function that converts uppercase to lowercase
    Args:
       str: a string of words
    return:
       sentence in uppercase
    """

    return str.lower()
if __name__ == "__main__":
    str = (input("Enter a string: "))
    print(lower(str))