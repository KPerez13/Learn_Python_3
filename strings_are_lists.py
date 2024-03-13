# Introduction to lists
# They're all Lists!
# 2 min

# A string can be thought of as a list of characters.

# Like any other list, each character in a string has an index. Consider the string:

# favorite_fruit = "blueberry"

# We can select specific letters from this string using the index. Let’s look at the first letter of the string.

# print(favorite_fruit[1])
# # Output: l

# Whoops, is that the first letter you expected? Notice that the letter at index 1 of "blueberry" isn’t b, it’s l. This is because the indices of a string start at 0. b is located at the zero index and we could select it using:

# print(favorite_fruit[0])
# # Output: b

# It’s important to note that indices of strings must be integers. If we were to try to select a non-integer index we would get a TypeError.

# For example:

# print(favorite_fruit[1.5])

# This would result in:

# Traceback (most recent call last):
#   File "script.py", line 3, in <module>
#     print(favorite_fruit[1.5])
# TypeError: string indices must be integers

# Task #1:
# One of the most common things that are represented by strings is names.

# Save your name as a string to the variable my_name.

# Answer:

my_name = "Kenny"

# Task #2:
# Select the first letter of the variable my_name and save it to first_initial.
# Answer:
first_initial = (my_name[0])
print(first_initial)
