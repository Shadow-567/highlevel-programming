#!/usr/bin/python3
"""a module that implements a basic calculator"""

calc = __import__("11-calc")


if __name__ == "__main__":
    print("Performing Arithmetic operations")
    op = int(input("Enter 1- add, 2- sub, 3- mul, 4- div, 5 -exp, 6 -mod: "))
    if op < 1 or op > 6:
        print("Invalid operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second nber: "))
    if op == 1:
        print(calc.add(num1, num2))
    elif op == 2:
        print(calc.sub(num1, num2))
    elif op == 3:
        print(calc.mul(num1, num2))
    elif op == 4:
        print(calc.div(num1, num2))
    elif op == 5:
        print(calc.exp(num1, num2))
    elif op == 6:
        print(calc.mod(num1, num2))