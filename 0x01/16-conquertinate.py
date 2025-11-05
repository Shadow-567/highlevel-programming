#!/usr/bin/python3
"""a  module that joins two strings together"""

def conatenate(str1, str2):
    """
    A function that takes two strings and combine them together
    Args:
       str1: first string to combine
       str2: second string to combine
    """
    return str1 + str2
if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    print((str1) + (str2))