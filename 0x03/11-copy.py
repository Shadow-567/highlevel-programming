#!/usr/bin/python3
"""a module that """

names = ["Benedict", "Daniel", "Kingsley"]

a = names
b = names[::]

a[0] = "Paul"

print(names)
print(b)