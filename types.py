# Types
# 5 min

# Python equips us with many different ways to store data. A float is a different kind of number from an int, and we store different data in a list than we do in a dict. These are known as different types. We can check the type of a Python variable using the
# type()
# Preview: Docs Loading link description
# function.

# a_string = "Cool String"
# an_int = 12

# print(type(a_string))
# # prints "<class 'str'>"

# print(type(an_int))
# # prints "<class 'int'>"

# Copy to Clipboard

# Above, we defined two
# variables
# Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
# , and checked the type of these two variables. A variable’s type determines what you can do with it and how you can use it. You can’t .get() something from an integer, just as you can’t add two
# dictionaries
# Preview: Docs Loading link description
# together using +. This is because those operations are defined at the type level.


# Instructions:
# .

# Call type() on the integer 5 and print the results.
# Checkpoint 2 Passed

# 2.

# Define a dictionary my_dict using curly braces {}.

# The dictionary can be empty, such as:

# empty_dict = {}

# Copy to Clipboard

# Checkpoint 3 Passed

# 3.

# Print out the type() of my_dict.
# Checkpoint 4 Passed

# 4.

# Define a list called my_list.
# Checkpoint 5 Passed

# 5.

# Print out the type() of my_list.



print(type(5))

my_dict = {}

print(type(my_dict))

my_list = []

print(type(my_list))