#!/usr/bin/python3
"""a module that reverse a word using loop"""

word = input("Enter a word: ")
reversed_word = ""

for i in word:
    reversed_word = i  + reversed_word

print(f"Original: {word}")
print(f"reversed_word: {reversed_word}")