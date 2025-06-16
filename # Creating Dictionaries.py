# Creating Dictionaries
# Introduction to Python Dictionaries
# 5 min

# A
# Preview: Docs Loading link description
# dictionary
# is an unordered set of key: value pairs.

# It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

# Suppose we want to store the prices of various items sold at a cafe:

#     Avocado Toast is 6 dollars
#     Carrot Juice is 5 dollars
#     Blueberry Muffin is 2 dollars

# In Python, we can create a dictionary called menu to store this data:

# menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Copy to Clipboard

# Notice that:

#     A dictionary begins and ends with curly braces { and }.
#     Each item consists of a key ("avocado toast") and a value (6).
#     Each key: value pair is separated by a comma.

# It’s considered good practice to insert a space ( ) after each comma, but our code will still run without the space.

# Instruction 1
# Suppose we have a dictionary of temperature sensors in the house and what temperatures they read. We’ve just added a sensor to the "pantry", and it reads 22 degrees.

# Add this pair to the dictionary on line 1.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}


# Instruction 2
# Remove the # in front of the definition of the dictionary num_cameras, which represents the number of cameras in each area around the house.

# If you run this code, you’ll get an error:

# SyntaxError: invalid syntax

# Try to find and fix the syntax error to make this code run.

num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)