#!/usr/bin/python3
"""a module that combines equations"""


price = float(input("Enter the price of the item: $"))
quantity = int(input("Enter the quantity of the item you want to buy"))

total_cost = price * quantity

print(f"You bought {quantity} items at ${price} each. Total cost: ${total_cost} ")