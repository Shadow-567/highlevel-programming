#!/usr/bin/python3
"""a module that calculates the fctorial"""

def factorial(n):
    """
    Calculate the factorial of a number using recursion
    Args:
        n: Integer to calculate factorial for
    Returns:
        Factorial of n
    """

    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print(result)