# Basic Operations:

# Create a set with at least five different numbers.
set1 = {1, 2, 3, 4, 5}
# Add an element to the set and remove an element from it.
set1.add(6)
set1.remove(5)
# Check if a given element exists in the set.
print(1 in set1)
# Set Operations:

# Write a Python program to find the union, intersection, and difference between two sets.
set2 = {1, 2, "Lucky", "Tadi", 10}


def union_intersection_difference_sets(set1, set2):
    print(f"Union: {set1.union(set2)}")
    print(f"Intersection: {set1.intersection(set2)}")
    return f"Difference: {set1.difference(set2)}"


print(union_intersection_difference_sets(set1, set2))
# Create two sets and determine if one is a subset of the other.
print(set1.issubset(set2))
# Unique Elements:

# Given a list with duplicate elements, convert it into a set to remove duplicates.
list1 = [1, 2, 1, 2, 3, 3, 4, 1, 5, 6, 20, 10]
set3 = set(list1)
print(set3)
# Mathematical Applications:

# Create sets representing students enrolled in two different courses and find students who are in both courses.
Data_science = {"Lucky", "Veera", "Venkat", "Prasad", "Purna"}
computer_science = {"Vikram", "Veera", "Karthik", "Lucky", "Surya"}
print(Data_science & computer_science)
print(Data_science.intersection(computer_science))
# Write a program to find common elements between three sets.
print(set1.intersection(set2, set3))
print(set1 & set2 & set3)
# Set Comprehension:

# Use set comprehension to create a set of squares of numbers from 1 to 10.
set_squares = {i**2 for i in range(1, 11)}
print(set_squares)
# Frozen Sets:

# Explain and demonstrate the use of a frozenset in Python.
# Frozen sets are immutable in nature. We cannot add, delete, update or modify the elements of a frozen sets.
frozen_set = frozenset(set3)
print(f"Frozen Set: {frozen_set}")
