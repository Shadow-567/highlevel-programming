#!/usr/bin/python3
"""a module that records student grades"""

def analyze_grades(grades):
    highest_grade = max(grade for _, grade in grades)
    
    top_students = [name for name, grade in grades if grade == highest_grade]

    average = sum(grade for _, grade in grades) / len(grades)

    below_average = [name for name, grade in grades if grade < average]

    return top_students, average, below_average

grades = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 92), ("Ethan", 67)]

top_students, average, below_average = analyze_grades(grades)

print("Top_students: ", top_students)
print("Average: ", round(average, 2))
print("Below average: ", below_average)