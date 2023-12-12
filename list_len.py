#Length

#Often, we’ll need to find the number of items in a list, usually called its length.

#We can do this using a built-in function called len().

#When we apply len() to a list, we get the number of elements in that list:

#my_list = [1, 2, 3, 4, 5]

#print(len(my_list))

#Would output:

#5

#Let’s find the length of various lists!


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below: 

#Calculate the length of long_list and save it to the variable long_list_len.

long_list_len = len(long_list)

print(long_list_len)

#Use print() to examine long_list_len., already completed in step 1, killing two birds with one stone :) 

#We have provided a completed range() function for the variable big_range.

#Calculate its length using the function len() and save it to a variable called big_range_length.

#Note: Range objects do not need to be converted to lists in order to determine their length

big_range_length = len(big_range)

#Use print() to examine big_range_length.
print(big_range_length)


