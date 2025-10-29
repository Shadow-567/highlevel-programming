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

    match op:
        case 1:
            print(f"Result: {calc.add(num1, num2)}")
        case 2:
            print(f"Result: {calc.sub(num1, num2)}")
        case 3:
            print(f"Result: {calc.mul(num1, num2)}")
        case 4:
            print(f"Result: {calc.div(num1, num2)}")
        case 5:
            print(f"Result: {calc.exp(num1, num2)}")
        case 6:
            print(f"Result: {calc.mod(num1, num2)}")