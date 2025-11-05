#!/usr/bin/python3
"""a module that combined two list together"""

even = range(0, 11, 2)
odd = range(1, 11, 2)

num = []

num.extend(odd)
num.extend(even)
print(num)