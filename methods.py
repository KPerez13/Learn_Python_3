# Introduction to Classes
# Methods
# 8 min

# Methods are
# functions
# Preview: Docs Loading link description
# that are defined as part of a class. The first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self. Methods always have at least this one argument.

# We define methods similarly to functions,
# except
# Preview: Docs Loading link description
# that they are indented to be part of the class.

# class Dog:
#   dog_time_dilation = 7

#   def time_explanation(self):
#     print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

# pipi_pitbull = Dog()
# pipi_pitbull.time_explanation()
# # Prints "Dogs experience 7 years for every 1 human year."

# Copy to Clipboard

# Above we created a Dog class with a .time_explanation() method that takes one argument, self, which refers to the object calling the function. We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.

# Notice we didn’t pass any arguments when we called .time_explanation(), but were able to refer to self in the function body. When you call a method it automatically passes the object calling the method as the first argument.


# Instructions:

# 1.

# At Jan van High, the students are constantly calling the school rules into question. Create a Rules class so that we can explain the rules.

# In order for your code to run, you have to have something in your class — you can’t have a defined class with no body like the following:

# class exampleClass:

# Copy to Clipboard

# For now, make the body of your class pass. This will allow your code to run without error.


# class Rules:
#   pass

# 2.

# Give Rules a method .washing_brushes() that returns the string

# "Point bristles towards the basin while washing your brushes."

# Copy to Clipboard

# Since we’ve now given this class a method, we can remove the pass that we added in the previous step.


class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."