#!/usr/bin/python3
"""a module that creates topples"""

fruits = ("Mango", "Orange", "Cashew", "Guava")

print(fruits)
print(len(fruits))
print(fruits[0])
print(type(fruits))

# add item to a tuple
new_fruits = fruits + ("Pawpaw", "Apple")

print(new_fruits)

#converting tuple to list

fruit_list = list(fruits)

print(type(fruit_list))