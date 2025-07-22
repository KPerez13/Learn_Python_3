# What's With "with"?
# 6 min

# We’ve been opening these files with this with block so far, but it seems a little weird that we can only use our file variable in the indented block. Why is that? The with keyword invokes something called a context manager for the file that we’re calling
# open()
# Preview: Docs Loading link description
# on. This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

# Why is closing the file so complicated? Well, most other aspects of our code deal with things that Python itself controls. All the
# variables
# Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
# you create: integers,
# lists
# Preview: Docs Loading link description
# ,
# dictionaries
# Preview: Docs Loading link description
# — these are all Python objects, and Python knows how to clean them up when it’s done with them. Since your files exist outside your Python script, we need to tell Python when we’re done with them so that it can close the connection to that file. Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file.

# The with syntax replaces older ways to access files where you need to call
# .close()
# Preview: Docs Loading link description
# on the file object manually. We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards.

# fun_cities_file = open('fun_cities.txt', 'a')

# # We can now append a line to "fun_cities".
# fun_cities_file.write("Montréal")

# # But we need to remember to close the file
# fun_cities_file.close()

# Copy to Clipboard

# In the above script we added “Montréal” as a new line in our file fun_cities.txt. However, since we used the older-style syntax, we had to remember to close the file afterwards. Since this is necessarily more verbose (requires at least one more line of code) without being any more expressive, using with is preferred.


# # Instructions
# 1.

# In script.py there’s a file object that doesn’t get closed correctly. Let’s fix it by changing the syntax!

# Remove this line:

# close_this_file = open('fun_file.txt')

# Copy to Clipboard

# And change it to use the with syntax from our previous exercises.

# Remember to indent the rest of the body so that we don’t get an IndentError.




with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
print(setup)
