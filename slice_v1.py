#Slicing Lists I

#In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

#Lets assume we have a list of letters:

#letters = ["a", "b", "c", "d", "e", "f", "g"]

#Suppose we want to select from "b" through "f".

#We can do this using the following syntax: letters[start:end], where:

    #start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
    #end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.

#sliced_list = letters[1:6]
#print(sliced_list)

#Would output:

#["b", "c", "d", "e", "f"]

#Notice that the element at index 6 (which is "g") is not included in our selection.



suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]

# Your code below: 
#Use print() to examine the variable beginning.
#Before hitting Run think about what elements beginning will contain?
print(beginning)

#Modify beginning, so that it selects the first 2 elements of suitcase.

beginning = suitcase[0:2]

#Create a new list called middle that contains the middle two items ( ["pants", "pants"] ) from suitcase.

#Print middle to see the slice!

middle = suitcase[2:4]
print(middle)


