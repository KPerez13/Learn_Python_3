# Python Code Challenges:
# Functions
#
# Challenge #1:
# 1. Tenth Power
#
# Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:
#
#     Set up the function header for tenth_power which accepts one parameter
#     Take the tenth power of the input value
#     Return the result
# Answer:
# Write your tenth_power function here:
def tenth_power(num):
  result = num ** 10
  return result
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
#
# Challenge 2:
# 2. Square Root
#
# Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. We need to:
#
#     Set up the function header for square_root which accepts one parameter
#     Take the square root of the input value
#     Return the result
# Write your square_root function here:
def square_root(num):
  return num ** 0.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# Challenge 3:
# 3. Win Percentage
#
# Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:
#
#     Define the function header with two parameters, wins and losses
#     Calculate the total number of games using the number of wins and losses
#     Get the ratio of winning using the number of wins out of the total number of games.
#     Convert the ratio to a percentage
#     Return the percentage
# Write your win_percentage function here:
def win_percentage(wins, losses):
  total_games = wins + losses
  winning_games = wins / total_games * 100
  return winning_games
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# Challenge 4:
# 4. Average
#
# Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:
#
#     Define the function with two input parameters, num1 and num2
#     Calculate the sum of the two numbers
#     Divide the sum by the number of inputs to the function
#     Return the answer
# Write your average function here:
def average(num1, num2):
  total = num1 + num2
  average_calculation = total / 2
  return average_calculation
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# Challenge 5
# 5. Remainder
#
# For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this we will need to:
#
#     Define the function to accept two parameters
#     Multiply the first input value by 2
#     Divide the second input value by 2
#     Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
#     Return the answer
# Write your remainder function here:
def remainder(num1, num2):
  numerator = num1 * 2
  denominator = num2 / 2
  result = numerator % denominator
  return result
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
