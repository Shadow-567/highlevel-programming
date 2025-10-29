#!/usr/bin/python3
"""a module that calcualtes quadratic equation"""


def quadratic(a, b, c):
    """
    A function that calculates quadratic equation
    Args:
        a: an unknown value required to find x1 and x2
        b: an unknown value required to find x1 and x2
        c: an unknown value required to find x1 and x2
   Return:
        x1 and x2
    """
    discriminant = b ** 2 - 4 * a * c
    
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)

    return x1, x2   

if __name__ == "__main__":
    a = float(input("Enter the value a: "))
    b = float(input("Enter the value b: "))
    c = float(input("Enter the value c: "))

    print(quadratic(a, b, c))