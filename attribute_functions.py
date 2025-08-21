# Attribute Functions
# 13 min

# Instance
# variables
# Preview: Docs Variables are used to store data that can be used and manipulated throughout a program.
# and class variables are both accessed similarly in Python. This is no mistake, they are both considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

# class NoCustomAttributes:
#   pass

# attributeless = NoCustomAttributes()

# try:
#   attributeless.fake_attribute
# except AttributeError:
#   print("This text gets printed!")

# # prints "This text gets printed!"

# Copy to Clipboard

# What if we aren’t sure if an object has an attribute or not?
# hasattr()
# Preview: Docs Loading link description
# will
# return
# Preview: Docs Loading link description
# True if an object has a given attribute and False otherwise. If we want to get the actual value of the attribute,
# getattr()
# Preview: Docs Returns the value of a named attribute from an object.
# is a Python function that will return the value of a given object and attribute. In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

# The syntax and parameters for these
# functions
# Preview: Docs Loading link description
# look like this:

# hasattr(object, “attribute”) has two parameters:

#     object : the object we are testing to see if it has a certain attribute
#     attribute : name of attribute we want to see if it exists

# getattr(object, “attribute”, default) has three parameters (one of which is optional):

#     object : the object whose attribute we want to evaluate
#     attribute : name of attribute we want to evaluate
#     default : the value that is returned if the attribute does not exist (note: this parameter is optional)

# Calling those functions looks like this:

# hasattr(attributeless, "fake_attribute")
# # returns False

# getattr(attributeless, "other_fake_attribute", 800)
# # returns 800, the default value

# Copy to Clipboard

# Above, we checked if the attributeless object has the attribute .fake_attribute. Since it does not, hasattr() returned False. After that, we used getattr to attempt to retrieve .other_fake_attribute. Since .other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.


# Instructions:
# 1.

# In script.py we have a list of different data types: a dictionary, a string, an integer, and a list all saved in the variable can_we_count_it.

# For every element in can_we_count_it, check if the element has the attribute .count using the hasattr() function. If so, print the following line of code:

# print(str(type(element)) + " has the count attribute!")

# Copy to Clipboard

# Checkpoint 2 Passed

# 2.

# Now let’s add an else statement for the elements that do not have the attribute .count. In this else statement add the following line of code:

# print(str(type(element)) + " does not have the count attribute :(")

# Copy to Clipboard

# Checkpoint 3 Passed

# 3.

# Let’s go over the terminal output of the past two instructions. You should see the following output in your terminal right now:

# <class 'dict'> does not have the count attribute :(
# <class 'str'> has the count attribute!
# <class 'int'> does not have the count attribute :(
# <class 'list'> has the count attribute!

# Copy to Clipboard

# This is because dictionaries and integers both do not have a .count attribute, while strings and lists do. In this exercise, we have iterated through can_we_count_it and used hasattr() to determine which elements have a .count attribute. We never actually used the .count() method, but you can read more about it
# here
# Preview: Docs Loading link description
# if you are curious about what it is.

# Click run to move onto the next exercise!

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
