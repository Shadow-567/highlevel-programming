#!/usr/bin/python3
"""a module that handles python string formatting"""

name = "Benedict"
age = 19
price = 49.99

formattedprice = "The price is {} dollars.".format(price)
formattedstring = "My name is {} and i am {} years old".format(name,age)

print(formattedprice)
print(formattedstring)