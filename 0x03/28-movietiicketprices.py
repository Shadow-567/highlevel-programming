#!/usr/bin/python3
"""a module that takes age and return the ticket price"""

age = int(input("Enter your age: "))
def ticket_price(age):
    
    if not isinstance(age, (int, float)) or age < 0:
        return "Invalid age"
    
    if age < 12:
        return 5
    elif 12 <= age <= 17:
        return 8
    elif 18 <= age <= 59:
        return 12
    elif age >= 60:
        return 6
    else:
        return "Ivalid age"
    
print(ticket_price(age))    