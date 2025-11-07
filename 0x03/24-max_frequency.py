#!/usr/bin/python3
"""a module that returns the string that appears most frequently"""


fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

def max_frequency(words):

    if not fruits:
        return None, 0
    
    freq = {}

    for word in fruits:
        freq[word] = freq.get(word, 0) + 1
    
    max_word = max(freq, key= freq.get)
    return max_word, freq[max_word]


result = max_frequency(fruits)
print(result)