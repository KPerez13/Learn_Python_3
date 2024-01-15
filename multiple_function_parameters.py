# Multiple Parameters

# Using a single parameter is useful but functions let us use as many parameters as we want! That way, we can pass in more than one input to our functions.

# We can write a function that takes in more than one parameter by using commas:

# def my_function(parameter1, parameter2, parameter3):
#   # Some code

# When we call our function, we will need to provide arguments for each of the parameters we assigned in our function definition.

# # Calling my_function
# my_function(argument1, argument2)

# For example take our trip application’s trip_welcome() function that has two parameters:

# def trip_welcome(origin, destination):
#   print("Welcome to Tripcademy")
#   print("Looks like you are traveling from " + origin)
#   print("And you are heading to " + destination)

# Our two parameters in this function are origin and destination. In order to properly call our function, we need to pass argument values for both of them.

# The ordering of your parameters is important as their position will map to the position of the arguments and will determine their assigned value in the function body (more on this in the next exercise!).

# Our function call could look like:

# trip_welcome("Prospect Park", "Atlantic Terminal")

# In this call, the argument value of "Prospect Park" is assigned to be the origin parameter, and the argument value of"Atlantic Terminal" is assigned to the destination parameter.

# The output would be:

# Welcome to Tripcademy
# Looks like you are traveling from Prospect Park
# And you are heading to Atlantic Terminal

# Let’s practice writing and calling a multiple parameter function!

# Write your code below: 

#Our travel application users want to calculate the total expenses they may have to incur on a trip.

# Task 1:
# Write a function called calculate_expenses (replace <function> with the function name) that will have four parameters (in exact order):

#     plane_ticket_price
#     car_rental_rate
#     hotel_rate
#     trip_time

# Each of these parameters will account for a different expense that our users will incur.

# Note: Like before, we will see an error: SyntaxError: unexpected EOF while parsing, since there is no code in the body of the function. In the next step we will add statements to the function.

# Task 2:
# Within the body of the function, let’s start to make some calculations for our expenses. First, let’s calculate the total price for a car rental.

# Create new variable called car_rental_total that is the product of car_rental_rate and trip_time.

# Task 3:
# Next, we want to apply the same logic but for our hotel_rate.

# Create new variable called hotel_total that is the product of hotel_rate and trip_time.

# We also have a coupon to give our users some cashback for their hotel visit so subtract 10 from that total in the same statement. Woohoo, coupons! 💵

# Task 4:
# Lastly, create a new variable called trip_total that is the sum of car_rental_total, hotel_total, and plane_ticket_price.

# Note: Do not delete return trip_total at the end of the function. This will output your new variable when the function is called.


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total

# Step 5: call your function with the following argument values for the parameters listed:

#     plane_ticket_price : 200
#     car_rental_rate : 100
#     hotel_rate : 100
#     trip_time: 5

# Be sure to call your function inside of print() so you can see the output.
print(calculate_expenses(200, 100, 100, 5))
