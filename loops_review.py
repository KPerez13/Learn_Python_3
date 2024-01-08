# Loops
# Review

# Good job! In this lesson, you learned

#     How to write a for loop.
#     How to use range in a loop.
#     How to write a while loop.
#     What infinite loops are and how to avoid them.
#     How to control loops using break and continue.
#     How to write elegant loops as list comprehensions.

# Let’s get some more practice with these concepts!

# Your code below:
# Task 1:
# Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = [0,1,2,3,4,5,6,7,8,9]

# Task 2:
# Create a for loop that goes through single_digits and prints out each one.
for digit in single_digits:
  print(digit)

# # Task 3:
# Before the loop, create a list called squares. Assign it to be an empty list to begin with.
squares = []

# # Task 4:
# Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

for digit in single_digits:
  squares.append(digit ** 2)

# Task 5:
# After the for loop, print out squares 
print(squares)

# Task 6:
# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

cubes = [digit ** 3 for digit in single_digits]

# Task 7:
# print cubes
# Good job! 
print(cubes)
