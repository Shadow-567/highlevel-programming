#!/usr/bin/python3
"""a module that convert scores to grade"""

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
elif score >= 60 and score < 69:
    print("Grade D")
elif score >= 0 and score < 59:
    print("Grade F")
else:
    print("Invalid score")