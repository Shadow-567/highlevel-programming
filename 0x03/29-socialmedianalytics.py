#!/usr/bin/python3
"""a module that tracks hashtags in posts"""

day_1 = ["#fun", "#travel", "#food", "#sunset", "#fun"]
day_2 = ["#work", "#food", "#travel", "#fitness"]

set_day_1 = set(day_1)
set_day_2 = set(day_2)

trending = set_day_1.intersection(set_day_2)

unique_day_1 = set_day_1 - set_day_2
unique_day_2 = set_day_2 - set_day_1

total_distinct = len(set_day_1.union(set_day_2))

print("Trending hashtags: ", trending)
print("Unique to Day 1: ", unique_day_1)
print("Unique Day 2: ", unique_day_2)
print("Total distinct hashtags: ", total_distinct)