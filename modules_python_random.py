# Modules in Python
# Modules Python Random
# 10 min

# datetime is just the beginning. There are hundreds of Python
# Preview: Docs A module is a Python file that contains functions, definitions, and statements that can be included in an application.
# modules
# that you can use. Another one of the most commonly used is
# Preview: Docs Loading link description
# random
# which allows you to generate numbers or select items at random.

# With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:

# import random

# Copy to Clipboard

# We’ll work with two common random functions:

#     Preview: Docs Loading link description
#     random.choice()
#     which takes a list as an argument and returns a number from the list
#     Preview: Docs Loading link description
#     random.randint()
#     which takes two numbers as arguments and generates a random number between the two numbers you passed in

# Let’s take randomness to a whole new level by picking a random number from a list of randomly generated numbers between 1 and 100.

# Task 1
# In script.py import the random library.

# Import random below:
import random

# Task 2
# Create a variable random_list and set it equal to an empty list


# Create random_list below:
random_list = []

# Task 3
# Turn the empty list into a list comprehension that uses random.randint() to generate a random integer between 1 and 100 (inclusive) for each number in range(101).


random_list = [random.randint(1,100) for x in range(101)]
# Create randomer_number below:

# Task 4
# Create a new variable randomer_number and set it equal to random.choice() with random_list as an argument.

randomer_number = random.choice(random_list)

# Task 5
# Print randomer_number below:
print(randomer_number)
