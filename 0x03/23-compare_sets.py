#!/usr/bin/python3
"""a module that takes two sets and return the tuple"""

def compare_sets(a, b):
    result = {}
    result.update(
        {"Union": a.union(b),
         "intersection": a.intersection(b),
        "a_difference_b": a.difference(b),
        "b_difference_a": b.difference(a)}
    )
    return result

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7, 8}

result = compare_sets(set_1, set_2)
print(result)