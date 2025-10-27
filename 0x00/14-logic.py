#!/usr/bin/python3
"""a module that perform logial equations"""

ans1 = bool(int(input("Is your name John? (1 or 0): ")))
ans2 = bool(int(input("Are you married? (1 or 0): ")))


print(f"{ans1} and {ans2} -> {ans1 and ans2}")
print(f"{ans1} or {ans2} -> {ans1 and ans2}")
print(f"not {ans1} -> {not ans1}")
print(f"not {ans2} -> {not ans2}")
print(f"not ({ans1} and {ans2}) -> {not(ans1 and ans2)}")
print(f"not ({ans1} or {ans2}) -> {not(ans1 or ans2)}")