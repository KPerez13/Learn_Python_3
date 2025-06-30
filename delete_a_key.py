# Delete a Key
# 12 min

# Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:

# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

# Copy to Clipboard

# When we get a ticket number, we want to
# Preview: Docs Loading link description
# return
# the prize and also remove that pair from the dictionary, since the prize has been given away. We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:

# print(raffle.pop(320291, "No Prize"))
# # Prints "Gift Basket"
# print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(100000, "No Prize"))
# # Prints "No Prize"
# print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
# print(raffle.pop(872921, "No Prize"))
# # Prints "Concert Tickets"
# print(raffle)
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}


# .pop() works to delete items from a dictionary, when you know the key value.


available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# Intruction #1
# You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.


available_items.pop("stamina grains", 15)

health_points += 15

# Instruction 2
# In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

health_points += 30 and available_items.pop("power stew", 30)

# Instruction 3
# In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

health_points += 0 and available_items.pop("mystic bread", 0)


# Instruction 4
# Print available_items and health_points.
# Learned you can print multiple items, by seperating them with commas

print(available_items, health_points)