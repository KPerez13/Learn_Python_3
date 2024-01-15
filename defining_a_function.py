# # Your code below: 
# Defining a Function

# A function consists of many parts, so let’s first get familiar with its core - a function definition.

# Here’s an example of a function definition:

# def function_name():
#   # functions tasks go here

# There are some key components we want to note here:

#     The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name in snake_case format that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.

#     Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on parameters later in the lesson!). In this example function, we have no parameters.

#     A colon : to mark the end of the function header.

#     Lastly, we have one or more valid python statements that make up the function body (where we have our python comment).

# Notice we’ve indented our # function tasks go here comment. Like loops and conditionals, code inside a function must be indented to show that they are part of the function.

# Here is an example of a function that greets a user for our trip planning application:

# def trip_welcome():
#   print("Welcome to Tripcademy!") 
#   print("Let's get you to your destination.")

# Note: Pasting this code into the editor and clicking Run will result in an empty output terminal. The print() statements within the function will not execute since our function hasn’t been used. We will explore this further in the next exercise; for now, let’s practice defining a function.

Task 1:
# Two of the most common NYC attractions include the Empire State Building and Times Square.

# In defining_a_function.py, we’ll write a function that prints the directions via subway from the Empire State Building to Times Square.

# First, define a function, directions_to_timesSq(). Leave the body of the function empty for now.

# Note: When we run the code, we will see an error: SyntaxError: unexpected EOF while parsing. This will occur when we don’t populate a function with any statements. We will populate it with code in the next step.

# EOF stands for “End of File” — Python is telling you that it was expecting some code in the body of the function, but it hit the end of the file first.

def directions_to_timesSq():

# # Task 2:
# Within the body of the function, use three print() statements to output the following directions:

# Walk 4 mins to 34th St Herald Square train station
# Take the Northbound N, Q, R, or W train 1 stop
# Get off the Times Square 42nd Street stop

# Remember, if you run your code, you shouldn’t see any output in the terminal at this point. Check out the hint if you want to see how to see the output (we will be doing it in the next section as well!)

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")

