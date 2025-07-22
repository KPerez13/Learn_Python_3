# Reading a CSV File
# 12 min

# Recall our CSV file from our last exercise:

# users.csv

# Name,Username,Email
# Roger Smith,rsmith,wigginsryan@yahoo.com
# Michelle Beck,mlbeck,hcosta@hotmail.com
# Ashley Barker,a_bark_x,a_bark_x@turner.com
# Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com

# Copy to Clipboard

# Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes. In Python we can convert that data into a dictionary using the csv library’s DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the above table:

# import csv

# list_of_email_addresses = []
# with open('users.csv', newline='') as users_csv:
#   user_reader = csv.DictReader(users_csv)
#   for row in user_reader:
#     list_of_email_addresses.append(row['Email'])

# Copy to Clipboard

# In the above code we first import our csv library, which gives us the tools to parse our CSV file. We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV. Then we open the users.csv file with the temporary variable users_csv.

# We pass the additional keyword argument newline='' to the file opening
# open()
# Preview: Docs Loading link description
# function so that we don’t accidentally mistake a line
# break
# Preview: Docs Loading link description
# in one of our data fields as a new row in our CSV (read more about this in the Python documentation).

# After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python
# dictionaries
# Preview: Docs A dictionary is a data set of key-value pairs.
# which we can use access methods for. The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.

# When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.

# Instructions

# 1.

# Import the csv module.
# Checkpoint 2 Passed

# 2.

# Open up the file cool_csv.csv in the temporary variable cool_csv_file.
# Checkpoint 3 Passed

# 3.

# Using csv.DictReader read the contents of cool_csv_file into a new variable called cool_csv_dict.
# Checkpoint 4 Passed

# 4.

# cool_csv.csv includes a cool fact about every person in the CSV.

# For each row in cool_csv_dict print out that row’s "Cool Fact".





import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])