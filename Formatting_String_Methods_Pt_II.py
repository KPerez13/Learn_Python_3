# .format() II
# 7 min

# .format() can be made even more legible for other people reading your code by including
# Preview: Docs Python keywords are reserved for specific purposes and not available for assignment.
# keywords
# . Previously, with .format(), you had to make sure that your
# Preview: Docs Loading link description
# variables
# appeared as arguments in the same order that you wanted them to appear in the string, which added unnecessary complications when writing code.

# By including keywords in the string, and in the arguments, you can remove that ambiguity. Let’s look at an example.

# def favorite_song_statement(song, artist):
#   return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

# Now it is clear to anyone reading the string what it is supposed to return, they don’t even need to look at the arguments of .format() in order to get a clear understanding of what is supposed to happen. You can even reverse the order of artist and song in the code above and it will work the same way.

# For example, if the arguments of .format() are in a different order, the code will still work since the keywords are present:

# def favorite_song_statement(song, artist):
#   # this will have the same output as the above example
#   return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)

# This makes writing AND reading the code much easier.


# Instructions #1
# The function poem_description is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.

# Fix the function by using keywords in the .format() method.


# Instructions #2
# Run poem_description with the following arguments and save the results to the variable my_beard_description:

# author = "Shel Silverstein"
# title = "My Beard"
# original_work = "Where the Sidewalk Ends"
# publishing_date = "1974"

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = (poem_description("1974","Shel Silverstien","My Beard", "Where the Sidewalk Ends"))