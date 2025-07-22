# What Is a CSV File?
# 5 min

# Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand.
# CSV
# Preview: Docs Loading link description
# files are an example of a text file that impose a structure to their data. CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format. A spreadsheet that looks like the following
# Name 	Username 	Email
# Roger Smith 	rsmith 	wigginsryan@yahoo.com
# Michelle Beck 	mlbeck 	hcosta@hotmail.com
# Ashley Barker 	a_bark_x 	a_bark_x@turner.com
# Lynn Gonzales 	goodmanjames 	lynniegonz@hotmail.com
# Jennifer Chase 	chasej 	jchase@ramirez.com
# Charles Hoover 	choover 	choover89@yahoo.com
# Adrian Evans 	adevans 	adevans98@yahoo.com
# Susan Walter 	susan82 	swilliams@yahoo.com
# Stephanie King 	stephanieking 	sking@morris-tyler.com
# Erika Miller 	jessica32 	ejmiller79@yahoo.com

# In a CSV file that same exact data would be rendered like this:

# users.csv

# Name,Username,Email
# Roger Smith,rsmith,wigginsryan@yahoo.com
# Michelle Beck,mlbeck,hcosta@hotmail.com
# Ashley Barker,a_bark_x,a_bark_x@turner.com
# Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
# Jennifer Chase,chasej,jchase@ramirez.com
# Charles Hoover,choover,choover89@yahoo.com
# Adrian Evans,adevans,adevans98@yahoo.com
# Susan Walter,susan82,swilliams@yahoo.com
# Stephanie King,stephanieking,sking@morris-tyler.com
# Erika Miller,jessica32,ejmiller79@yahoo.com

# Copy to Clipboard

# Notice that the first row of the CSV file doesn’t actually represent any data, just the labels of the data that’s present in the rest of the file. The rest of the rows of the file are the same as the rows in the spreadsheet software, just instead of being separated into different cells they’re separated by… well I suppose it’s fair to say they’re separated by commas.

# Instructions:
# 1.

# CSV files are just plain text files!

# Open logger.csv using our standard with syntax, saving the file object in the temporary variable log_csv_file.
# Checkpoint 2 Passed

# 2.

# Print out the contents of logger.csv by calling .read() on the file. Notice that it is parsed as a string.



with open('logger.csv') as log_csv_file:
  contents = log_csv_file.read()
print(contents)