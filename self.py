# Introduction to Classes
# Self
# 16 min

# Since we can already use
# dictionaries
# Preview: Docs Loading link description
# to store key-value pairs, using objects for that purpose is not really useful. Instance
# variables
# Preview: Docs Variables are used to store data that can be used and manipulated throughout a program.
# are more powerful when you can guarantee a rigidity to the data the object is holding.

# This convenience is most apparent when the constructor creates the instance variables using the arguments passed into it. If we were creating a search engine and wanted to create a class to hold each search entry, we could do so like this:

# class SearchEngineEntry:
#   def __init__(self, url):
#     self.url = url

# codecademy = SearchEngineEntry("www.codecademy.com")
# wikipedia = SearchEngineEntry("www.wikipedia.org")

# print(codecademy.url)
# # prints "www.codecademy.com"

# print(wikipedia.url)
# # prints "www.wikipedia.org"

# Copy to Clipboard

# In the preceding code sample, we define a SearchEngineEntry class, which contains a constructor with two parameters, self and url. Inside the constructor body, we create an instance variable named self.url and assign it the value of the url parameter that is passed into the constructor.

# We then create the codecademy instance of SearchEngineEntry by passing the URL as an argument to the constructor. After codecademy is defined, printing codecademy.url shows that the URL has been assigned to the url instance variable of codecademy. Similarly, wikipedia.url holds the value that was passed into the constructor when wikipedia was defined.

# Since the self keyword refers to the object and not the class being called, we can define a .secure() method on the SearchEngineEntry class that returns the secure link to an entry.

# class SearchEngineEntry:
#   secure_prefix = "https://"
#   def __init__(self, url):
#     self.url = url

#   def secure(self):
#     return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

# codecademy = SearchEngineEntry("www.codecademy.com")
# wikipedia = SearchEngineEntry("www.wikipedia.org")

# print(codecademy.secure())
# # prints "https://www.codecademy.com"

# print(wikipedia.secure())
# # prints "https://www.wikipedia.org"

# Copy to Clipboard

# Above, we define our .secure() method to take just the one required argument, self. We access both the class variable self.secure_prefix and the instance variable self.url to
# return
# Preview: Docs Loading link description
# a secure URL.

# This is the strength of writing object-oriented programs. We can write our
# classes
# Preview: Docs Loading link description
# to structure the data that we need and write methods that will interact with that data in a meaningful way.



# Instructions:
# 1.

# In script.py you’ll find our familiar friend, the Circle class.

# Even though we usually know the diameter beforehand, what we need for most calculations is the radius.

# In Circle‘s constructor, set the instance variable self.radius to equal half the diameter that gets passed in.
# Checkpoint 2 Passed

# 2.

# Define a new method .circumference() for your circle object that takes only one argument, self, and returns the circumference of a circle with the given radius by this formula:

# circumference = 2 * pi * radius

# Copy to Clipboard

# Checkpoint 3 Passed

# 3.

# Define three Circles with three different diameters.

#     A medium pizza, medium_pizza, that is 12 inches across.
#     Your teaching table, teaching_table, which is 36 inches across.
#     The Round Room auditorium, round_room, which is 11,460 inches across.

# Checkpoint 4 Passed

# 4.

# Print out the circumferences of medium_pizza, teaching_table, and round_room.



class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = (diameter/2)
  def circumference(self):
    return 2 * self.pi * self.radius
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())