# Replace
# 4 min

# The next string method we will cover is
# Preview: Docs Loading link description
# .replace()
# . Replace takes two arguments and replaces all instances of the first argument in a string with the second argument. The syntax is as follows

# string_name.replace(substring_being_replaced, new_substring)

# Great! Let’s put it in context and look at an example.

# with_spaces = "You got the kind of loving that can be so smooth"
# with_underscores = with_spaces.replace(' ', '_')
# print(with_underscores)
# # 'You_got_the_kind_of_loving_that_can_be_so_smooth'

# Here we used .replace() to change every instance of a space in the string above to be an underscore instead.

# Note that in this example, we used a single character, but these
# Preview: Docs Loading link description
# substrings
# can be multiple characters long!

# Instrucions #1
# The poetry organization has sent over the bio for Jean Toomer as it currently exists on their site. Notice that there was a mistake with his last name and all instances of Toomer are lacking one o.

# Use .replace() to change all instances of Tomer in the bio to Toomer. Save the updated bio to the string toomer_bio_fixed.



toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

print(toomer_bio_fixed)
