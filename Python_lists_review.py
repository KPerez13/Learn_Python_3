#Review

#In this lesson, we learned how to:

    #Add elements to a list by index using the .insert() method.
    #Remove elements from a list by index using the .pop() method.
    #Generate a list using the range() function.
    #Get the length of a list using the len() function.
    #Select portions of a list using slicing syntax.
    #Count the number of times that an element appears in a list #using the .count() method.
    #Sort a list of items using either the .sort() method or sorted#() function.

#As you go through the exercises, feel free to use print() to see changes when not explicitly asked to do so.

#Task1:
#Our friend Jiho has been so successful in both the flower and #grocery business that she has decided to open a furniture store.

#Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

#First, how many items are in the warehouse?

#Save the answer to a variable called inventory_len.

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

#Task2:
#Select the first element in inventory. Save it to a variable called first.
first = (inventory[0])
print(first)

#Task3:
#Select the last element from inventory. Save it to a variable called last.
last = (inventory[-1])
print(last)

#Task 4:
#Select items from the inventory starting at index 2 and up to, but not including, index 6.
#Save your answer to a variable called inventory_2_6.
#index 2 = "headboard" and index6 = "dresser" but up to so maybe "table"?
inventory_2_6= (inventory[2:6])
print(inventory_2_6)

#Task 5:
#Select the first 3 items of inventory. Save it to a variable called first_3.
# let's try a negative slice 
first_3 = (inventory[:-16])
print(first_3)

#Task 6:
#How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.
twin_beds = (inventory.count('twin bed'))
print(twin_beds)

#Task 7:
#Remove the 5th element in the inventory. Save the value to a variable called removed_item. 
removed_item = (inventory.pop(4))
print(inventory)

#Task 8:
#There was a new item added to our inventory called "19th Century Bed Frame". 
#Use the .insert() method to place the new item as the 11th element in our inventory.
inventory.insert(10,"19th Century Bed Frame")
print(inventory)

#Task 9:
#Sort inventory using the .sort() method or the sorted() function.
#Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().
#Print inventory to see the result 
inventory.sort()
print(inventory)
