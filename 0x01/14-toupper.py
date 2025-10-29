#!/usr/bin/python3
"""a module that converts lowercase to uppercase"""

def toupper(str):
    """
    A function that convert lowercase  to uppercase
    Args:
        str: a string of words passed to be converted to upper
    Return:
        sentence in uppercase
    """
    return str.upper()
if __name__ == "__main__":
    str = input("Enter a string: ")
    print(toupper(str))