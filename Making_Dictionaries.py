# Creating Dictionaries
# Make a Dictionary
# 4 min

# In the previous exercise, we saw a dictionary that maps
# Preview: Docs Loading link description
# strings
# to numbers (i.e., "avocado toast": 6). However, the keys can be numbers as well.

# For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:

# subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

# Copy to Clipboard

# Values can be of any
# Preview: Docs Loading link description
# type
# . We can use a string, a number, a list, or even another dictionary as the value associated with a key!

# For example:

# students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

# Copy to Clipboard

# The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in that class.

# We can also mix and match key and value types. For example:

# person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

#Instruction #1:
# Create a dictionary called translations that maps the following words in English to their definitions in Sindarin (the language of the elves):
# English 	Sindarin
# mountain 	orod
# bread 	bass
# friend 	mellon
# horse 	roch

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}