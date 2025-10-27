#!/usr/bin/python3
"'""a module that performs comparison operations"""


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} -> {num1 == num2}")
print("{} != {} -> {}".format(num1, num2, num1 != num2))
print(f"{num1} > {num2} -> {num1 > num2}")
print(f"{num1} < {num2} -> {num1 < num2}")
print(f"{num1} >= {num2} -> {num1 >= num2}")
print(f"{num1} <= {num2} -> {num1 <= num2}")