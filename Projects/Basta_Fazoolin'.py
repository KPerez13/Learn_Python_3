class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

class Franchise:
  def __init__(self,address, menus):
     self.address = address
     self.menus = menus
  
  def __str__(self):
    return f'{self.name} menu available from {self.start_time} to {self.end_time}'

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total


    

brunch_menu = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu('brunch', brunch_menu, 11, 16)

early_bird_menu = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird = Menu('early_bird', early_bird_menu, 15, 18)

dinner_menu = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner = Menu('dinner', dinner_menu, 17, 23)

kids_menu = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids = Menu('kids', kids_menu, 11, 21)




# print(brunch)
# Task 10 by the way:
# Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
# test_menu = ['pancakes', 'home fries', 'coffee']
# print(brunch.calculate_bill(test_menu))


# # Task 11:
# # What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
# second_test_menu = ['salumeria plate', 'mushroom ravioli (vegan)']
# print(early_bird.calculate_bill(second_test_menu))