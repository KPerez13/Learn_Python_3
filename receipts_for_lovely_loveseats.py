
# This is a scenario where we opened up a furnitre store called "Lovely Loveseats for Neat Suites on Fleet Street"
# This is meant to create items, descriptions, prices as well as tax and print out reciepts for customers 

# First Item and it's description 
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# Setting price for the first item
lovely_loveseat_price = 254.00

# Second Item and it's description 
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black"

# Second Item and it's price 
stylish_settee_price = 180.50

# Third Item and it's description  
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Third Item and it's price 
luxurious_lamp_price = 52.15

# Sales Tax 
sales_tax = .088

# customer_one_total that is going to have prices added to it
customer_one_total = 0

# Description of items they're getting 
customer_one_itemization = ""

# Adding in customer's first item 
customer_one_total += lovely_loveseat_price

# Adding in item description 
customer_one_itemization += lovely_loveseat_description 

# Adding in second item :) 
customer_one_total += luxurious_lamp_price

# Adding in second item description 
customer_one_itemization += luxurious_lamp_description

# Calculating Sales Tax 
customer_one_tax = customer_one_total * sales_tax

# Adding Sales Tax 
customer_one_total += sales_tax 

# printing out customer items 
print("Customer One Items:")

print(customer_one_itemization)

#printing out customer total 
print("Customer One Total:")

print(customer_one_total)


# And just like that we have our second python project! 
