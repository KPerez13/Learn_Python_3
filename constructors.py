# Introduction to Classes
# Constructors
# 12 min

# There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic,” because they behave differently from regular methods. Another popular term is
# dunder methods
# Preview: Docs Dunder methods use a special syntax to perform class-specific operations in Python.
# , so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

# The first dunder method we’re going to use is the
# __init__()
# Preview: Docs Loading link description
# method (note the two underscores before and after the word “init”). This method is used to initialize a newly created object. It is called every time the class is instantiated.

# Methods that are used to prepare an object being instantiated are called constructors. The word “constructor” is used to describe similar features in other object-oriented programming languages, but programmers who refer to a constructor in Python are usually talking about the __init__() method.

# class Shouter:
#   def __init__(self):
#     print("HELLO?!")

# shout1 = Shouter()
# # prints "HELLO?!"

# shout2 = Shouter()
# # prints "HELLO?!"

# Copy to Clipboard

# Above, we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout. Don’t worry, this doesn’t hurt the computer at all.

# Pay careful attention to the instantiation syntax we use. Shouter() looks a lot like a function call, doesn’t it? If it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by the __init__() method.

# class Shouter:
#   def __init__(self, phrase):
#     # make sure phrase is a string
#     if type(phrase) == str:

#       # then shout it out
#       print(phrase.upper())

# shout1 = Shouter("shout")
# # prints "SHOUT"

# shout2 = Shouter("shout")
# # prints "SHOUT"

# shout3 = Shouter("let it all out")
# # prints "LET IT ALL OUT"

# Copy to Clipboard

# Above, we’ve updated our Shouter class to take the additional parameter phrase. When we created each of our objects, we passed an argument to the constructor. The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.


#Instructions

# 1.

# Add a constructor to our Circle class.

# Since we seem more frequently to know the diameter of a circle, it should take the argument diameter.

# It doesn’t need to do anything yet, just write pass in the body of the constructor.


# class Circle:
#   pi = 3.14
#   def __init__(self, diameter):
#     pass


# 2.

# Now have the constructor print out the message "New circle with diameter: {diameter}" when a new circle is created.

# Create a circle teaching_table with diameter 36.



class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")



teaching_table = Circle(36)