# Review
# 29 min

# Excellent work! This lesson has shown you the vast variety of string methods and their power. Whatever the problem you are trying to solve, if you are working with strings then string methods are likely going to be part of the solution.

# Over this lesson you’ve learned:

#     Preview: Docs Loading link description
#     .upper()
#     ,
#     Preview: Docs Takes in a string and returns a copy of the string formatted in the title case: each word in the string is capitalized.
#     .title()
#     , and
#     Preview: Docs Takes a string, and returns a copy of that string in which all letters are lowercase. Numbers and symbols are not changed.
#     .lower()
#     adjust the casing of your string.
#     Preview: Docs Loading link description
#     .split()
#     takes a string and creates a list of
#     Preview: Docs Loading link description
#     substrings
#     .
#     .join() takes a list of strings and creates a string.
#     Preview: Docs Loading link description
#     .strip()
#     cleans off whitespace, or other noise from the beginning and end of a string.
#     Preview: Docs Loading link description
#     .replace()
#     replaces all instances of a character/string in a string with another character/string.
#     Preview: Docs Loading link description
#     .find()
#     searches a string for a character/string and returns the index value that character/string is found at.
#     .format() allows you to interpolate a string with
#     Preview: Docs Loading link description
#     variables
#     .

# Well I’ve been stringing you along for long enough, let’s get some more practice in!

# Instructions #1
#  Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.

# First, start by printing highlighted_poems to the terminal and see how it displays.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

# Instruction #2
# The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.

# Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

highlighted_poems_list = highlighted_poems.split(",")

#Instruction #3
# Print highlighted_poems_list, how does the structure of the data look now?
print(highlighted_poems_list)


#Instruction #4
# Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.

# Start by creating a new empty list, highlighted_poems_stripped.

# Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

highlighted_poems_stripped = []
for whitespace in highlighted_poems_list:
  stripped_list = whitespace.strip()
  highlighted_poems_stripped.append(stripped_list)

  print(highlighted_poems_stripped)

#Instruction #6:
# Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.

# Create a new empty list called highlighted_poems_details.
highlighted_poems_details = []

#Instructinon #7:
# Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.
for string in highlighted_poems_stripped:
  new_string = string.split(":")
  highlighted_poems_details.append(new_string)


#Instruction #8:
# Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.

# Create three new empty lists, titles, poets, and dates.


#Instruction #9:
# Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

# For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.

titles = []
poets = []
dates = []

for details in highlighted_poems_details:
  titles.append(details[0])
  poets.append(details[1])
  dates.append(details[2])

#Instructions #10
# Finally, write a for loop that uses .format() to print out the following string for each poem:

for string in highlighted_poems_details:
  intial_string = "The poem {} was published by {} in {}"
  string[0]
  string[1]
  string[2]
  formatted_string = intial_string.format(string[0], string[1], string[2])
  print(formatted_string)
