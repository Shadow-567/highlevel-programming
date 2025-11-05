#!/usr/bin/python3
"""a module that handles matrix creation"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def sum_matrix(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

total = sum_matrix(matrix)
print(f"\nTotal sum of all elements: {total}")