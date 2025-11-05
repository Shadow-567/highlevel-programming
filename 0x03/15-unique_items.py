#!/usr/bin/python3
"""a module that uses unique items"""

def remove_duplicates(my_list):
    unique_list = []
    
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
        
    return unique_list

numbers_with_duplicate = [1, 2, 2, 3, 4, 4, 5]
print("Original list with duplicates:", numbers_with_duplicate)

cleaned_list = remove_duplicates(numbers_with_duplicate)
print("Cleaned list:", cleaned_list)