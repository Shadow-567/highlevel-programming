#!/usr/bin/python3
"""a module that displays prime numbers"""


for i in range(2, 51):
    is_prime = True
    
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    
    if is_prime:
        print(i, end=", ")