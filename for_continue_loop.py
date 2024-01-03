# Loop Control: Continue

# While the break control statement will come in handy, there are other situations where we don’t want to end the loop entirely. What if we only want to skip the current iteration of the loop?

# Let’s take this list of integers as our example:

# big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# What if we want to print out all of the numbers in a list, but only if they are positive integers. We can use another common loop control statement called continue.

# for i in big_number_list:
#   if i <= 0:
#     continue
#   print(i)

# This would produce the output:

# 1
# 2
# 4
# 5
# 2

# Notice a few things:

#     Similar to when we were using the break control statement, our continue control statement is usually paired with some form of a conditional (if/elif/else).
#     When our loop first encountered an element (-1) that met the conditions of the if statement, it checked the code inside the block and saw the continue. When the loop then encounters a continue statement it immediately skips the current iteration and moves onto the next element in the list (4).
#     The output of the list only printed positive integers in the list because every time our loop entered the if statement and saw the continue statement it simply moved to the next iteration of the list and thus never reached the print statement.

# Let’s continue learning about control statements with some exercises!

# Task 1:
# Your computer is the doorman at a bar in a country where the drinking age is 21.

# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
