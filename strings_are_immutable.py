# Strings are Immutable
# 4 min

# So far in this lesson, we’ve been selecting characters from strings, slicing strings, and concatenating strings. Each time we perform one of these operations we are creating an entirely new string.

# This is because strings are immutable. This means that we cannot change a string once it is created. We can use it to create other strings, but we cannot change the string itself.

# This property, generally, is known as mutability. Data types that are mutable can be changed, and data types, like strings, that are immutable cannot be changed.

first_name = "Bob"
last_name = "Daily"

# Task 1:
# The most recent hire at Copeland’s Corporate Company is a fellow named Rob Daily. Unfortunately, Human Resources seem to have made a bit of a typo and sent over the wrong first_name.

# Try changing the first character of first_name by running
# first_name[0] = "R"

# Task 2:
# Oh right! Strings are immutable, so we can’t change an individual character. Okay that’s no problem—we can still fix this!

# Delete the code you just wrote for step 1.

# Then, concatenate the string "R" with a slice of first_name that includes everything but the first character, "B", and save it to a new string fixed_first_name.
fixed_name = "R"
adjust_name = first_name[-2:]
fixed_first_name = fixed_name + adjust_name 
