#For Loops: Using Range

#Often we won’t be iterating through a specific list (or any collection), but rather only want to perform a certain action multiple times.

#For example, if we wanted to print out a "Learning Loops!" message six times using a for loop, we would follow this structure:

#for <temporary variable> in <list of length 6>:
  #print("Learning Loops!")

#Notice that we need to iterate through a list with a length of six, but we don’t necessarily care what is inside of the list.

#To create arbitrary collections of any length, we can pair our for loops with the trusty Python built-in function range().

#An example of how the range() function works, this code generates a collection of 6 integer elements from 0 to 5:

#six_steps = range(6)

# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5

#We can then use the range directly in our for loops as the collection to perform a six-step iteration:

#for temp in range(6):
  #print("Learning Loops!")

#Would output:

#Learning Loops!
#Learning Loops!
#Learning Loops!
#Learning Loops!
#Learning Loops!
#Learning Loops!

#Something to note is we are not using temp anywhere inside of the loop body. If we are curious about which #loop iteration (step) we are on, we can use temp to track it. Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.

#for temp in range(6):
 # print("Loop is on iteration number " + str(temp + 1))

#Would output:

#Loop is on iteration number 1
#Loop is on iteration number 2
#Loop is on iteration number 3
#Loop is on iteration number 4
#Loop is on iteration number 5
#Loop is on iteration number 6

#Let’s try out using a range in a for loop!


promise = "I will finish the python loops module!"

# Task 1: Use the range() function in a for loop to print() out the provided promise variable five times.

for mistletoe in range(5):
  print(promise)
