# Basic String Manipulation:

# Assign the string "Hello, World!" to a variable and print it.

# Create a string "Python Programming" and extract the first five characters using slicing.

# String Methods:

# Given a string "python is fun", convert it to uppercase.

# Replace "fun" with "awesome" in the string "Python is fun".

# String Formatting:

# Use f-string formatting to create a message like "My name is John, and I am 25 years old.", where the name and age are variables.

# Given a price of 49.99, format it to display only two decimal places.

# String Functions:

# Count the occurrences of the letter 'o' in "Hello, how are you?".

# Find the position of "world" in "Hello, world! Python is amazing.".

# Reverse and Check:

# Reverse the string "Python" using slicing.

# Check if "madam" is a palindrome (a word that reads the same forward and backward).
str1 = "Hello, World!"
print(str1)
str2 = "Python Programming"
print(str2[:5])
str3 = "python is fun"
print(str3.upper())
str3.replace("fun", "awesome")
name = "John"
age = 25
print(f"My name is {name}, and I am {age} years old.")
price = 49.99
print("{:.2f}".format(price))
str4 = "Hello, How are you?"
print(str4.count('o'))
str5 = "Hello, World! Python is amazing"
print(str5.index("World"))
str6 = "Python"
print(str6[::-1])
str7 = "madam"
if str7 == str7[::-1]:
    print(f"{str7} is a Palindrome")
else:
    print(f"{str7} is not a Palindrome")
