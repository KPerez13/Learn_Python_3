# Loop Control: Break

# Loops in Python are very versatile. Python provides a set of control statements that we can use to get even more control out of our loops.

# Let’s take a look at a common scenario that we may encounter to see a use case for loop control statements.

# Take the following list items_on_sale as our example:

# items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

# It’s often the case that we want to search a list to check if a specific value exists. What does our loop look like if we want to search for the value of "knit dress" and print out "Found it" if it did exist?

# It would look something like this:

# for item in items_on_sale:
#   if item == "knit dress":
#     print("Found it")

# This code goes through each item in items_on_sale and checks for a match. This is all fine and dandy but what’s the downside?

# Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Unfortunately, our loop will keep running until we reach the end of the list.

# Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case but what if items_on_sale had 1000 items? What if it had 100,000 items? This would be a huge waste of time for our program!

# Thankfully you can stop iteration from inside the loop by using break loop control statement.

# When the program hits a break statement it immediately terminates a loop. For example:

# items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

# print("Checking the sale list!")

# for item in items_on_sale:
#   print(item)
#   if item == "knit dress":
#     break

# print("End of search!")

# This would produce the output:

# Checking the sale list!
# blue shirt
# striped socks
# knit dress
# End of search!

# When the loop entered the if statement and saw the break it immediately ended the loop. We didn’t need to check the elements of "red headband" or "dinosaur onesie" at all.

# Now let’s break some loops!

# Task 1:
# You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.

# Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.

# Use the <temporary variable> name of dog_breed in your loop declaration.

# Task 2:
# Inside your for loop, after you print each dog breed, check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"

# Task 3:
# Add a break statement when your loop has found dog_breed_I_want so that the rest of the list does not need to be checked once we have found our breed.

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
  if dog_breed == "Collie":
    break

