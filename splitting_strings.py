# string Methods
# Splitting Strings
# 3 min

# Preview: Docs Loading link description
# .upper()
# ,
# Preview: Docs Takes a string, and returns a copy of that string in which all letters are lowercase. Numbers and symbols are not changed.
# .lower()
# , and
# Preview: Docs Takes in a string and returns a copy of the string formatted in the title case: each word in the string is capitalized.
# .title()
# all are performed on an existing string and produce a string in return. Let’s take a look at a string method that returns a different object entirely!

# Preview: Docs Loading link description
# .split()
# is performed on a string, takes one argument, and returns a list of
# Preview: Docs A substring is a sequence of characters that are part of an original string.
# substrings
# found between the given argument (which in the case of .split() is known as the delimiter). The following syntax should be used:

# string_name.split(delimiter)

# If you do not provide an argument for .split() it will default to splitting at spaces.

# For example, consider the following strings:

# man_its_a_hot_one = "Like seven inches from the midday sun"
# print(man_its_a_hot_one.split())
# # => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

# .split() returned a list with each word in the string. Important to note: if we run .split() on a string with no spaces, we will get a single element array containing the same string. 


# Instructions #1
# In the code editor is a string of the first line of the poem Spring Storm by William Carlos Williams.

# Use .split() to create a list called line_one_words that contains each word in this line of poetry.

line_one = "The sky has given over"

line_one_words = line_one.split()
