# Built-in Functions vs User Defined Functions

# There are two distinct categories for functions in the world of Python. What we have been writing so far in our exercises are called User Defined Functions - functions that are written by users (like us!).

# There is another category called Built-in functions - functions that come built into Python for us to use. Remember when we were using print or str? Both of these functions are built into the language for us, which means we have been using built-in functions all along!

# There are lots of different built-in functions that we can use in our programs. Take a look at this example of using len() to get the length of a string:

# destination_name = "Venkatanarasimharajuvaripeta"

# # Built-in function: len()
# length_of_destination = len(destination_name)

# # Built-in function: print()
# print(length_of_destination)

# Would output the value of length_of_destination:

# 28

# Here we are using a total of two built-in functions in our example: print(), and len().

# And yes, if you’re wondering, that is a real railway station in India!

# There are even more obscure ones like help() where Python will print a link to documentation for us and provide some details:

# help("string")

# Would output (shortened for readability):

# NAME
#     string - A collection of string constants.

# MODULE REFERENCE
#     https://docs.python.org/3.8/library/string
    
#     The following documentation is automatically generated from the Python
#     source files.  It may be incomplete, incorrect or include features that
#     are considered implementation detail and may vary between Python
#     implementations.  When in doubt, consult the module reference at the
#     location listed above.
# .....

# Check out all the latest built-in functions in the official Python docs.

# Let’s practice using a few of them. You will need to rely on the provided Python documentation links to find your answers!

# Task 1:
# We were provided a list of prices for some gift shop items:

#     T-shirt: 9.75
#     Shorts: 15.50
#     Mug: 5.99
#     Poster: 2.00

# Create a variable called max_price and call the built-in function max() with the variables of prices to get the maximum price.

# Print max_price.

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)

print(max_price)

#Task 2:
# Using the same set of prices, create a new variable called min_price and use the built-in function min() with the variables of prices to get the minimum price.

# Print min_price.
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)

print(min_price)

# Task 3:
# Use the built-in function round() to round the price of the variable tshirt_price by one decimal place.

# Save the result to a variable called rounded_price and print it.

rounded_price = round(tshirt_price, 1)
print(rounded_price)
