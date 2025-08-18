# Methods with Arguments
# 12 min

# Methods can also take more arguments than just self:

# class DistanceConverter:
#   kms_in_a_mile = 1.609
#   def how_many_kms(self, miles):
#     return miles * self.kms_in_a_mile

# converter = DistanceConverter()
# kms_in_5_miles = converter.how_many_kms(5)
# print(kms_in_5_miles)
# # prints "8.045"

# Copy to Clipboard

# Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. Notice again that even though .how_many_kms() takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).


# Instructions:
# 1.

# It’s March 14th (known in some places as Pi day) at Jan van High, and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.

# Create a Circle class with class variable .pi. Set .pi to the approximation 3.14.
# Checkpoint 2 Passed

# 2.

# Give Circle an .area() method that takes two parameters: self and radius.

# Return the area as given by this formula:

# area = pi * radius ** 2

# Copy to Clipboard

# Checkpoint 3 Passed

# 3.

# Create an instance of Circle. Save it into the variable circle.
# Checkpoint 4 Passed

# 4.

# You go to measure several circles you happen to find around.

#     A medium pizza that is 12 inches across.
#     Your teaching table which is 36 inches across.
#     The Round Room auditorium, which is 11,460 inches across.

# You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area.

# Remember that the .radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.





class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()



pizza_class = Circle()
pizza_radius = 12 / 2
pizza_area = pizza_class.area(pizza_radius)

table_class = Circle()
table_radius = 36 / 2
teaching_table_area = table_class.area(table_radius)

room_class = Circle()
room_radius = 11460 / 2
round_room_area = room_class.area(room_radius)


