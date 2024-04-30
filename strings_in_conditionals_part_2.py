# Strings and Conditionals (Part Two)
# 15 min

# There’s an even easier way than iterating through the entire string to determine if a character is in a string. We can do this type of check more efficiently using in. in checks if one string is part of another string.

# Here is what the syntax of in looks like:

# letter in word

# Here, letter in word is a boolean expression that is True if the string letter is in the string word. Here are some examples:

# print("e" in "blueberry")
# # => True
# print("a" in "blueberry")
# # => False

# In fact, this method is more powerful than the function you wrote in the last exercise because it not only works with letters, but with entire strings as well.

# print("blue" in "blueberry")
# # => True
# print("blue" in "strawberry")
# # => False

# It can be helpful to include more than one boolean expression in the same line of code. To do this, use and or and not in between the boolean expressions.

# print("e" in "blueberry" and "e" in "carrot")
# # => False
# print("e" in "blueberry" and not "e" in "carrot")
# # => True

# The first example above is False because ONE of the expressions was False; there is no “e” in “carrot”. The second example is True because there is an “e” in “blueberry” and not an “e” in “carrot”; both expressions are True.

# Task 1:
# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.

# For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.

def contains(big_string,little_string):
  result = (little_string in big_string)
  return result 

# Task 2:
# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
# def common_letters(string_one, string_two):

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)

  return common







