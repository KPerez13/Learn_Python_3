# List Comprehensions: Introduction

# So far we have seen many of the ideas about using loops in our code. Python prides itself on allowing programmers to write clean and elegant code. We have already seen this with Python giving us the ability to write while and for loops in a single line.

# In this exercise, we are going to examine another way we can write elegant loops in our programs using list comprehensions.

# To start, let’s say we had a list of integers and wanted to create a list where each element is doubled. We could accomplish this using a for loop and a new list called doubled:

# numbers = [2, -1, 79, 33, -45]
# doubled = []

# for number in numbers:
#   doubled.append(number * 2)

# print(doubled)

# Would output:

# [4, -2, 158, 66, -90]

# Let’s see how we can use the power of list comprehensions to solve these types of problems in one line. Here is our same problem but now written as a list comprehension:

# numbers = [2, -1, 79, 33, -45]
# doubled = [num * 2 for num in numbers]
# print(doubled)

# Let’s break down our example in a more general way:

# new_list = [<expression> for <element> in <collection>]

# In our doubled example, our list comprehension:

#     Takes an element in the list numbers
#     Assigns that element to a variable called num (our <element>)
#     Applies the <expression> on the element stored in num and adds the result to a new list called doubled
#     Repeats steps 1-3 for every other element in the numbers list (our <collection>)

# Our result would be the same:

# [4, -2, 158, 66, -90]

# Task 1:
# We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.

# Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]

# Task 2:
# Print scaled_grades
print(scaled_grades)
