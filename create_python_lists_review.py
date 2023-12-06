# Your code below: # Your code below: 
#Task1
#Maria is entering customer data for her web store business. We’re going to help her organize her data.
#Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:
#Ainsley
#Ben
#Chani
#Depak

first_names=["Ainsley", "Ben", "Chani", "Depak"]

#Task2 
#Maria wants to track all customer’s preferred sizes for her clothing. Create a list called preferred_size.
#Fill our new list preferred_size with the following data, containing the preferred sizes for Ainsley, Ben, and Chani:
preferred_size=["Small", "Large", "Medium"]

#Task3
#Oh no! We forgot to add Depak’s size.
#Depak’s size is "Medium". Use .append() to add "Medium" to the preferred_size list.
#Print preferred_size to see our change.
preferred_size.append("Medium")
print(preferred_size)

#Task4:
#Maria is having a hard time visualizing which customer is associated with each size. Let’s restructure our two lists into a two-dimensional list to help Maria.
#In addition to our already available data, Maria is adding a third value for each customer that reflects if they want expedited shipping on their orders.
#This will be reflected using a boolean value (True for expedited, False for regular)
#Create a two-dimensional list called customer_data using the following table as a reference for the data. Each sublist should contain a name, size, and expedited shipping option for a single person.
#Name 	Size 	Expedited Shipping
#"Ainsley" 	"Small" 	True
#"Ben" 	"Large" 	False
#"Chani" 	"Medium" 	True
#"Depak" 	"Medium" 	False
#Print customer_data to see the data.

customer_data=[["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

#Task5
#"Chani" reached out to Maria. She requested to switch to regular shipping to save some money.
#Change the data value for "Chani"‘s shipping preference to False in our two-dimensional list to reflect the change.
customer_data[2][2]= False

#Task6
#"Ben" reached out to Maria asking to remove his shipping option (the True or False value) because he is unsure what type he wants.
#Use the .remove() method to delete the shipping value from the sublist that contains Ben’s data.
#Note: We never explicitly went over how to use the .remove() method on a 2d list together. If you feel like you are struggling, look at the hint for guidance. 
customer_data=[["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", False], ["Depak", "Medium", False]]
customer_data[1].remove(False)
print(customer_data)

#Task7
#Great job making it this far! One last thing, Maria received new customers, "Amit" and "Karim", the following 2d list contains their data: 
#[["Amit", "Large", True], ["Karim", "X-Large", False]]
#Create a new variable customer_data_final. Combine our existing list customer_data with our new customer 2d list using + by adding it to the end of customer_data.
#Print customer_data_final to see our final result.
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
