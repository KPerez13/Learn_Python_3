# Reading a File
# 7 min

# Computers use file systems to store and retrieve data. Each
# file
# Preview: Docs Files are named locations on disk to store related information that can be used in Python.
# is an individual container of related information. If you’ve ever saved a document, downloaded a song, or even sent an email you’ve created a file on some computer somewhere. Even script.py, the Python program you’re editing in the learning environment, is a file.

# So, how do we interact with files using Python? We’re going to learn how to read and write different kinds of files using code. Let’s say we had a file called real_cool_document.txt with these contents:

# real_cool_document.txt

# Wowsers!

# We could read that file like this:

# script.py

# with open('real_cool_document.txt') as cool_doc:
#   cool_contents = cool_doc.read()
# print(cool_contents)

# This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. Then we print cool_contents, which outputs the statement Wowsers!.


# Instruction #1
# Use with to open the file welcome.txt. Save the file object as text_file.

# Instruction #2
# Read the contents of text_file and save the results in text_data

# Instruction #3
# Print out text_data.

with open('welcome.txt') as text_file:
   text_data = text_file.read()
print(text_data)