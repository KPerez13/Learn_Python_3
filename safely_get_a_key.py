# Safely Get a Key
# 6 min

# We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError. This solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our dictionary!

# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will
# Preview: Docs Ends a function and sends a value back to the caller.
# return
# None by default:

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# #this line will return 632:
# building_heights.get("Shanghai Tower")

# #this line will return None:
# building_heights.get("My House")

# Copy to Clipboard

# You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:

# print(building_heights.get('Shanghai Tower', 0)) # Prints 632
# print(building_heights.get('Mt Olympus', 0)) # Prints 0
# print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'



user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Instruction #1
# Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called tc_id. Print tc_id to the console.

tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)


# Instruction #2
# Now let’s try getting a key that doesn’t exist!

# Use .get() to get the value of "superStackSmash"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called stack_id. Print stack_id to the console.

stack_id = user_ids.get('superStackSmash', 100000)

print(stack_id)