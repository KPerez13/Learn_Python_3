# More and More String Slicing (How Long is that String?)
# 10 min

# Python comes with some built-in functions for working with strings. One of the most commonly used of these functions is len(). len() returns the number of characters in a string:

# favorite_fruit = "blueberry"

# length = len(favorite_fruit)

# print(length)
# # Output: 9

# If you are taking the length of a sentence the spaces are counted as well.

# fruit_sentence = "I love blueberries"

# print(len(fruit_sentence))
# # Output: 18

# len() comes in handy when we are trying to select characters from the end of a string. What is the index of the last character,"y", of favorite_fruit from above? You can try to run the following code:

# last_char = favorite_fruit[len(favorite_fruit)]

# print(last_char)

# This will result in:

# IndexError: string index out of range

# Why does this generate an IndexError? Because the indices start at 0, so the final character in favorite_fruit has an index of 8. len(favorite_fruit) returns 9 and, because there is no value at that index, an IndexError occurs.

# Instead, the last character in a string has an index that is len(string_name) - 1.

# last_char = favorite_fruit[len(favorite_fruit)-1]

# print(last_char)
# # Output: y

# You could also slice the last several characters of a string using len():

# length = len(favorite_fruit)
# last_chars = favorite_fruit[length-4:]
# print(last_chars)
# # Output: erry

# Using a len() statement as the starting index and omitting the final index lets you slice n characters from the end of a string, where n is the amount you subtract from len().


first_name = "Reiko"
last_name = "Matsuki"

# Task 1:
# Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.

# Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.

def password_generator(first_name, last_name):
  first_length = len(first_name)
  last_three = first_name[first_length-3:]
  second_length = len(last_name)
  second_three = last_name[second_length-3:]
  return last_three + second_three

# Second Task:
temp_password = password_generator(first_name, last_name)

