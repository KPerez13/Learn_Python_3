# Modules Python Introduction
# 5 min

# In the world of programming, we care a lot about making code reusable. In most cases, we write code so that it can be reusable for ourselves. But sometimes we share code that’s helpful across a broad range of situations.

# In this lesson, we’ll explore how to use tools other people have built in Python that are not included automatically for you when you install Python. Python allows us to package code into
# Preview: Docs Loading link description
# files
# or
# Preview: Docs Stores unordered collections of unique elements.
# sets
# of files called
# Preview: Docs A module is a Python file that contains functions, definitions, and statements that can be included in an application.
# modules
# .

# A module is a collection of Python declarations intended broadly to be used as a tool. Modules are also often referred to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

# Usually, to use a module in a file, the basic syntax you need at the top of that file is:

# from module_name import object_name

# Copy to Clipboard

# Often, a library will include a lot of code that you don’t need that may slow down your program or conflict with existing code. Because of this, it makes sense to only import what you need.

# One common library that comes as part of the Python Standard Library is
# Preview: Docs Loading link description
# datetime
# . datetime helps you work with dates and times in Python.

# Let’s get started by importing and using the datetime module. In this case, you’ll notice that datetime is both the name of the library and the name of the object that you are importing.

# Import datetime from datetime below:
# Task 1:
# In script.py import the datetime type from the datetime library.

from datetime import datetime

# Task 2
# Create a variable current_time and set it equal to datetime.now().

current_time = datetime.now()

#Task 3
print(current_time)