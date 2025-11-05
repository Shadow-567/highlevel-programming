#!/usr/bin/python3
"""a module that deals with index"""

students = ["Alice", "Bob", "Charlie", "David"]

name_to_find = input("Who are you looking for? ")

if name_to_find in students:
    position = students.index(name_to_find)
    print(f"Yes, {name_to_find} is a student #{position + 1}")
else:
    print(f" {name_to_find} is not a student")