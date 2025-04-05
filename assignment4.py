# Tuple Creation

# Create a tuple named my_tuple containing at least five different elements (mix of integers, strings, and a float).
my_tuple = (1, 2, "Lucky", "Prasad", 76.5)

# Print the tuple.
print(my_tuple)
# Accessing Elements
print(*my_tuple)
for i in my_tuple:
    print(i)
# Print the first and last element of my_tuple using indexing.
print(my_tuple[0])
print(my_tuple[-1])
# Use negative indexing to access the second last element.
print(my_tuple[-2])
# Tuple Slicing
print(my_tuple[2:4])
# Slice and print the first three elements of my_tuple.
print(my_tuple[:3])
# Slice and print the last two elements.
print(my_tuple[: -3: -1])
# Tuple Operations
my_tup = (1, 2, 3, 4, 5)
print(len(my_tup))
print(max(my_tup))
print(min(my_tup))
print(sum(my_tup))
# Concatenate my_tuple with another tuple and print the result.
print(my_tuple+my_tup)
# Repeat my_tuple twice and print the result.
print(my_tuple*2)
# Tuple Methods
print(my_tuple.index("Lucky"))
print(my_tuple.count(2))
# Find the index of a specific element in my_tuple and print it.
print(my_tuple.index(1))
# Count the occurrences of a specific element in my_tuple and print it.
print(my_tuple.count("Prasad"))
# Tuple Immutability

# Try changing one element in my_tuple and observe
# my_tuple[2] = 6 I tried this and it returned an error.
"""The error is 
TypeError: 'tuple' object does not support item assignment
"""
