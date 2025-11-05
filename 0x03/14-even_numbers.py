#!/usr/bin/python3
"""a module that gets even number from a list"""

def get_even_numbers(numbers):
    even_list = []

    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    
    return even_list

my_numbers = [2, 5, 8, 11, 14, 17]
print("All numbers:", my_numbers)

even_ones = get_even_numbers(my_numbers)
print("Even numbers only:", even_ones)