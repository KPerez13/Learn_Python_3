# While Loops: Introduction

# In Python, for loops are not the only type of loops we can use. Another type of loop is called a while loop and is a form of indefinite iteration.

# A while loop performs a set of instructions as long as a given condition is true.

# The structure follows this pattern:

# while <conditional statement>:
  #<action>

# Let’s examine this example, where we print the integers 0 through 3:

# count = 0
# while count <= 3:
  # Loop Body
  #print(count)
  #count += 1

#Let’s break the loop down:

    #count is initially defined with the value of 0. The conditional statement in the while loop is count <= 3, which is true at the initial iteration of the loop, so the loop body executes.

#Inside the loop body, count is printed and then incremented by 1.

    #When the first iteration of the loop has finished, Python returns to the top of the loop and checks the conditional again. After the first iteration, count would be equal to 1 so the conditional still evaluates to True and so the loop continues.

    #This continues until the count variable becomes 4. At that point, when the conditional is tested it will no longer be True and the loop will stop.

#The output would be:

#0
#1
#2
#3

#Note the following about while loops before we write our own:

    #Indentation:

    #Notice that in our example the code under the loop declaration is indented. Similar to a for loop, everything at the same level of indentation after the while loop declaration is run on every iteration of the loop while the condition is true.

#while count <= 3:
   # Loop Body
   #print(count)
   #count += 1
   # Any other code at this level of indentation will
   # run on each iteration

#If we ever forget to indent, we’ll get an IndentationError or unexpected behavior.

    #Elegant loops:

#Similar to for loops, Python allows us to write elegant one-line while loops. Here is our previous example in a single line:

#count = 0
#while count <= 3: print(count); count += 1

#Note: Here we separate each statement with a ; to denote a separate line of code.

#Let’s practice writing a while loop!


# While Loop Walkthrough
# count = 0
# print("Starting While Loop")
# while count <= 3:
#   # Loop Body
#   # Print if the condition is still true
#   print("Loop Iteration - count <= 3 is still true")
#   # Print the current value of count 
#   print("Count is currently " + str(count))
#   # Increment count
#   count += 1
#   print(" ----- ")
# print("While Loop ended")

# Task 1:
#Examine the while loop from the narrative up above.There are additional print() statements to help visualize the iterations.

#Run the code to see what happens on each iteration of the loop. When you are finished, comment out the example to make space for the rest of the checkpoints.

#To quickly comment out the code, use your cursor or mouse to highlight all the code and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.

#If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise, you may have an infinite loop! If the stop condition for our loop is never met, we will create an infinite loop which stops our program from running anything else. To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.

# Let’s write a while loop that counts down from 10 to 0(inclusive). Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".

# As we saw in the narrative, our key components will be:

#     A variable to keep track of the count, and also help our loop eventually stop.

#     A condition that our while loop will check on each iteration.

#     Several code statements to execute on each iteration of the loop.

# Let’s tackle the first component!

# Create a variable named countdown and set the value to 10.

countdown = 10

# Now let’s tackle the actual while loop. Define a while loop that will run while our countdown variable is greater than or equal to zero.

# On each iteration:

#     We should print() the value of the countdown variable.
#     We should decrease the value of the countdown variable by 1

# Make sure to only print the value of countdown.

while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")
