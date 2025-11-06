#!/usr/bin/python3
"""a module that checks if a word is a PALINDROME"""

word = input("Enter a word: ").lower()

reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

if word == reversed_word:
    print("Word is a PALINDROME")

else:
    print("Word is not a PALINDROME")