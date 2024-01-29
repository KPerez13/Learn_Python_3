# Challenge 1. Append Size
#
# For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:
#
#     Define the function to accept one parameter for our list
#     Get the length of the list
#     Append the length of the list to the end of the list
#     Return the modified list

# Create a function called append_size that has one parameter named my_list.
#
# The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.
#
# For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

# Answer:
#Write your function here

def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# Challenge 2. Append Sum
#
# Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:
#
#     Define the function to accept one parameter for our list of numbers
#     Add the last and second-to-last elements from our list together
#     Append the calculated value to the end of our list.
#     Repeat steps 2 and 3 two more times
#     Return the modified list
# Write a function named append_sum that has one parameter — a list named named my_list.
#
# The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.
#
# For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
#Write your function here
def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# Challenge 3: Larger List
# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:
#
#     Define the function to accept two parameters for our two lists of numbers
#     Check if the length of the first list is greater than or equal to the length of the second list
#     If true, then return the last element from the first list. Otherwise, return the last element from the second list
# Write a function named larger_list that has two parameters named my_list1 and my_list2.
#
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.
# Hint
# Remember that we can use len(my_list1) to get the length of a list called my_list1. Also, to get the last element of my_list1 we can use my_list1[-1].
# Answer:
#Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Challenge 4: More Than N
# Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). The function will return True if the snack we are searching for appears more times than we provided as our third parameter. These are the steps we need:
#
#     Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
#     Count the number of occurrences of item (the second parameter) in my_list (the first parameter)
#     If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False
# Create a function named more_than_n that has three parameters named my_list, item, and n.
#
# The function should return True if item appears in the list more than n times. The function should return False otherwise.
#Write your function here
def more_than_n(my_list, item, n):
  occurences = my_list.count(item)
  if occurences > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Challenge 5: Combine Sort
# Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:
#
#     Define the function to accept two parameters, one for each list.
#     Combine the two lists together
#     Sort the result
#     Return the sorted and combined list
# Write a function named combine_sort that has two parameters named my_list1 and my_list2.
#
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.
#Write your function here
def combine_sort(my_list1, my_list2):
  my_combined_list = my_list1 + my_list2
  my_combined_list.sort()
  return my_combined_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
