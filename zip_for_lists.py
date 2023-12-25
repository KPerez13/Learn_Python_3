# Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.

# Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.

# Print list_of_names_and_dogs_names.

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners,dogs_names)

converted_zip = list(names_and_dogs_names)

print(converted_zip)
