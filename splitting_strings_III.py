# We can also split
# Preview: Docs Loading link description
# strings
# using escape sequences. Escape sequences are used to indicate that we want to split by something in a string that is not necessarily a character. The two escape sequences we will cover here are

#     \n Newline
#     \t Horizontal Tab

# Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by tabs. \t is particularly useful when dealing with certain datasets because it is not uncommon for data points to be separated by tabs.

# Let’s take a look at an example of splitting by an escape sequence:

# smooth_chorus = \
# """And if you said, "This life ain't good enough."
# I would give my world to lift you up
# I could change my life to better suit your mood
# Because you're so smooth"""

# chorus_lines = smooth_chorus.split('\n')

# print(chorus_lines)

# This code is splitting the multi-line string at the newlines (\n) which exist at the end of each line and saving it to a new list called chorus_lines. Then it prints chorus_lines which will produce the output:

# ['And if you said, "This life ain\'t good enough."', 'I would give my world to lift you up', 'I could change my life to better suit your mood', "Because you're so smooth"]

# The new list contains each line of the original string as its own smaller string. Also, notice that Python automatically escaped the ' character in the first line and adjusted to double quotation marks to allow the apostrophe on last line when it created the new list. 



spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""


# Instructions:
# The organization has sent you over the full text for William Carlos Williams poem Spring Storm. They want you to break the poem up into its individual lines.

# Create a list called spring_storm_lines that contains a string for each line of Spring Storm.

spring_storm_lines = spring_storm_text.split('\n')

print(spring_storm_lines)
