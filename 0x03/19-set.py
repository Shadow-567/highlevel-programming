#!/usr/bin/python
"""a module that creates a set"""

a = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}
b = {5, 6, 7}
print(a)
print(type(a))

# set operations

print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(a.isdisjoint(b))

# set methods

a.add(3)
print(f"After adding: {a}")
a.remove(2)
print(f"After removing: {a}")
a.pop()
print(f"After popping: {a}")
a.clear()
print(f"After clearing: {a}")