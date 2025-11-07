#!/usr/bin/python3
"""a module that counts vowel"""

def count_vowels(s):
    vowels = "a, e, i, o, u"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count

result = count_vowels("programming")
print(result)