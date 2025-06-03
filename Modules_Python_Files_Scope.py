# Modules in Python
# Modules Python Files and Scope
# 5 min

# You may remember the concept of
# Preview: Docs Loading link description
# scope
# from when you were learning about
# Preview: Docs Functions allow tasks to be performed multiple times within a program without having to be rewritten.
# functions
# in Python. If a variable is defined inside of a function, it will not be accessible outside of the function.

# Scope also applies to
# Preview: Docs Loading link description
# classes
# and to the
# Preview: Docs Loading link description
# files
# you are working within.

# Files have scope? You may be wondering.

# Yes. Even files inside the same directory do not have access to each other’s
# Preview: Docs Loading link description
# variables
# , functions, classes, or any other code. So if I have a file sandwiches.py and another file hungry_people.py, how do I give my hungry people access to all the sandwiches I defined?

# Well, files are actually modules, so you can give a file access to another file’s content using that glorious import statement.

# With a single line of from sandwiches import sandwiches at the top of hungry_people.py, the hungry people will have all the sandwiches they could ever want.


# Import library below:

# Task 1
# Tab over to library.py and define a function always_three() with no parameters that returns 3.

from library import always_three

# Task 2:
# Call your always_three() function in script.py. Check out that error message you get in the output terminal and the consequences of file scope. 
# Call your function below:

# Task 3
# Resolve the error with an import statement at the top of script.py that imports your function from library. Run your code and watch import do its magic!


always_three()