# Negative Indices
# 4 min

# In the previous exercise, we used len() to get a slice of characters at the end of a string.

# There’s a much easier way to do this — we can use negative indices! Negative indices count backward from the end of the string, so string_name[-1] is the last character of the string, string_name[-2] is the second last character of the string, etc.

# Here are some examples:

# favorite_fruit = 'blueberry'
# print(favorite_fruit[-1])
# # => 'y'

# print(favorite_fruit[-2])
# # => 'r'

# print(favorite_fruit[-3:])
# # => 'rry'

# Notice that we are able to slice the last three characters of ‘blueberry’ by having a starting index of -3 and omitting a final index.


company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# Task 1:
# Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.
second_to_last = company_motto[-2]

# Task 2:
# Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word. 
final_word = company_motto[-4:]
