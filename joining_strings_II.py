# Joining Strings II
# 5 min

# In the last exercise, we joined together a list of words using a space as the delimiter to create a sentence. In fact, you can use any string as a delimiter to join together a list of
# Preview: Docs Loading link description
# strings
# . For example, if we have the list

# santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']

# We could join this list together with ANY string. One often used string is a comma , because then we can create a string of comma-separated values, or CSV.

# santana_songs_csv = ','.join(santana_songs)
# print(santana_songs_csv)
# # => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# You’ll often find data stored in CSVs because it is an efficient, simple file type used by popular programs like Excel or Google Spreadsheets.

# You can also join using escape sequences as the delimiter. Consider the following example:

# smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

# smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

# print(smooth_fifth_verse)

# This code is taking the list of strings and joining them using a newline \n as the delimiter. Then it prints the result and produces the output:

# Well I'm from the barrio
# You hear my rhythm on your radio
# You feel the turning of the world so soft and slow
# Turning you 'round and 'round


winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']


winter_trees_full = '\n'.join(winter_trees_lines)

# print(winter_trees_full)
