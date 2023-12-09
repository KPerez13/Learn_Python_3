#Intersting note/lesson here:
#Often, we want to create a list of consecutive numbers in our programs. For example, suppose we want a list containing the numbers 0 through 9:

#my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo that can cause an error.

#Python gives us an easy way of creating these types of lists using a built-in function called range().

#The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.

#So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

#my_range = range(10)
#print(my_range)

#Would output:

#range(0, 10)

#Notice something different? The range() function is unique in that it creates a range object. It is not a typical list like the ones we have been working with.

#In order to use this object as a list, we have to first convert it using another built-in function called list().

#The list() function takes in a single input for the object you want to convert.

#We use the list() function on our range object like this:

#print(list(my_range))

#Would output:

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Your code below: 
#Task 1
#Modify number_list so that it is a range containing numbers starting at 0 and up to, but not including, 9.
number_list = range(0,9)
print(list(number_list))

# Task 2
# Create a range called zero_to_seven with the numbers 0 through 7.
#Print the result in list form.
zero_to_seven = range(0,8)
print(list(zero_to_seven))
