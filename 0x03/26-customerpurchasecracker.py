#!/usr/bin/python3
"""a module that keeps tracks of goods"""

customer1 = ["milk", "bread", "eggs", "bread", "butter"]
customer2 = ["bread", "butter", "cheese", "milk"]

def find_unique(cust1, cust2):
    return set(cust1 + cust2)

def find_common(cust1, cust2):
    return set(cust1).intersection(set(cust2))

def total_unique(cust1, cust2):
    return len(find_unique(cust1, cust2))

if __name__ == "__main__":
    unique = find_unique(customer1, customer2)
    common = find_common(customer1, customer2)
    total = total_unique(customer1, customer2)

    print(f"Unique items: {unique}")
    print(f"Common items: {common}")
    print(f"Total unique items: {total}")