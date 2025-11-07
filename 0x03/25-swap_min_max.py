#!/usr/bin/python3
"""a module that swaps the smallest number with the largest number in a list"""

numbers = [4, 9, 2, 7, 5]

def swap_min_max(numbers):

    min_index = numbers.index(min(numbers))

    max_index = numbers.index(max(numbers))

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    return numbers

result = swap_min_max(numbers)
print(result)