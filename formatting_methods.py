# String Methods
# Formatting Methods
# 6 min

# There are three string methods that can change the casing of a string. These are
# Preview: Docs Takes a string, and returns a copy of that string in which all letters are lowercase. Numbers and symbols are not changed.
# .lower()
# ,
# Preview: Docs Loading link description
# .upper()
# , and
# Preview: Docs Loading link description
# .title()
# .

#     .lower() returns the string with all lowercase characters.
#     .upper() returns the string with all uppercase characters.
#     .title() returns the string in title case, which means the first letter of each word is capitalized.

# Here’s an example of .lower() in action:

# favorite_song = 'SmOoTH'
# favorite_song_lowercase = favorite_song.lower()
# print(favorite_song_lowercase)
# # => 'smooth'

# Every character was changed to lowercase! It’s important to remember that string methods can only create new strings, they do not change the original string.

# print(favorite_song)
# # => 'SmOoTH'

# See, it’s still the same! These string methods are great for sanitizing user input and standardizing the formatting of your strings.

# Instruction #1
# You’re a programmer working for an organization that is trying to digitize and store poetry called Preserve the Verse.

# You’ve been given two strings, the title of a poem and its author, and have been asked to reformat them slightly to fit the conventions of the organization’s database.

# Make poem_title have title case and save it to poem_title_fixed.

# Instruction #2
# Print poem_title and poem_title_fixed.

# How did the string change?

# Instruction #3
# The organization’s database also needs the author’s name to be uppercase only.

# Make poem_author uppercase and save it to poem_author_fixed.

# Instruction #4
# Print poem_author and poem_author_fixed.

# Again, how did the string change?


poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
