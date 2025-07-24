# Reading a JSON File
# 7 min

# CSV isn’t the only file format that Python has a built-in library for. We can also use Python’s file tools to read and write
# JSON
# Preview: Docs Loading link description
# . JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript. The name, like CSV is a bit of a misnomer — some JSON is not valid JavaScript (and plenty of JavaScript is not valid JSON).

# JSON’s format is endearingly similar to Python dictionary syntax, and so JSON
# files
# Preview: Docs Loading link description
# might be easy to read from a Python developer standpoint. Nonetheless, Python comes with a json package that will help us parse JSON files into actual Python
# dictionaries
# Preview: Docs Loading link description
# . Suppose we have a JSON file like the following:

# purchase_14781239.json

# {
#   'user': 'ellen_greg',
#   'action': 'purchase',
#   'item_id': '14781239',
# }

# Copy to Clipboard

# We would be able to read that in as a Python dictionary with the following code:

# json_reader.py

# import json

# with open('purchase_14781239.json') as purchase_json:
#   purchase_data = json.load(purchase_json)

# print(purchase_data['user'])
# # Prints 'ellen_greg'

# Copy to Clipboard

# First we import the json package. We opened the file using our trusty
# open()
# Preview: Docs Loading link description
# command. Since we’re opening it in read-mode we just need to pass the file name. We save the file in the temporary variable purchase_json.

# We
# continue
# Preview: Docs Loading link description
# by parsing purchase_json using json.load(), creating a Python dictionary out of the file. Saving the results into purchase_data means we can interact with it. We print out one of the values of the JSON file by keying into the purchase_data object.


# Instructions 
# 1.

# Let’s read a JSON file! Start by importing the json module.
# Checkpoint 2 Passed

# 2.

# Open up the file message.json, saving the file object to the variable message_json.

# Open the file in read-mode, without passing any additional arguments to open().
# Checkpoint 3 Passed

# 3.

# Pass the JSON file object as an argument to json.load() and save the resulting Python dictionary as message.
# Checkpoint 4 Passed

# 4.

# Print out message['text'].


import json

with open('message.json') as message_json:
  message = json.load(message_json)
print(message['text'])