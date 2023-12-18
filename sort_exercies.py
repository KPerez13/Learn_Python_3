#Sorting Lists I

#Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

#We can sort a list using the method .sort().

#Suppose that we have a list of names:

#names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

#Let’s see what happens when we apply .sort():

#names.sort()
#print(names)

#Would output:

#['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

#As we can see, the .sort() method sorted our list of names in alphabetical order.

#.sort() also provides us the option to go in reverse. Instead of sorting in ascending order like we just saw, we can do so in descending order.

#names.sort(reverse=True)
#print(names)

#Would output:

#['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

#Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable.

#Let’s experiment sorting various lists!

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
# Use .sort() to sort addresses.
addresses.sort()
#Use print() to see how addresses changed.
print(addresses)
# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

