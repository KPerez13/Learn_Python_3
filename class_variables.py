# Class Variables
# 5 min

# When we want the same data to be available to every instance of a class we use a class variable. A class variable is a variable that’s the same for every instance of the class.

# You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class
# variables
# Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
# with object.variable syntax.

# class Musician:
#   title = "Rockstar"

# drummer = Musician()
# print(drummer.title)
# # prints "Rockstar"

# Copy to Clipboard

# Above we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.

# If we defined another musician, like guitarist = Musician() they would have the same .title attribute.

# NOTE: Class variables are often referenced with a leading period, like .title above. This is done to quickly show that the variable belongs to a class and must be accessed with dot notation, like drummer.title.

# Instructions:

# 1.

# You are digitizing grades for Jan van Eyck High School and Conservatory. At Jan van High, as the students call it, 65 is the minimum passing grade.

# Create a Grade class with a class attribute .minimum_passing equal to 65.


class Grade:
  minimum_passing = 65