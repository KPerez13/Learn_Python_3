# Modules in Python
# Modules Python Namespaces
# 15 min

# Notice that when we want to invoke the randint() function we call random.randint(). This is default behavior where Python offers a namespace for the module. A namespace isolates the
# Preview: Docs Loading link description
# functions
# ,
# Preview: Docs Loading link description
# classes
# , and
# Preview: Docs Loading link description
# variables
# defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

# Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

# Fortunately, this name can be altered by aliasing using the as keyword:

# import module_name as name_you_pick_for_the_module

# Copy to Clipboard

# Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.

# You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything. This syntax is considered dangerous because it could pollute our local namespace. Pollution occurs when the same name could apply to two possible things. For example, if you happen to have a function floor() focused on floor tiles, using from math import * would also import a function floor() that rounds down floats.

# Let’s combine your knowledge of the random library with another fun library called matplotlib, which allows you to plot your Python code in 2D.

# You’ll use a new random function random.sample() that takes a range and a number as its arguments. It will return the specified number of random numbers from that range.

# #random.sample takes a list and randomly selects k items from it
# new_list = random.sample(list, k)
# #for example:
# nums = [1, 2, 3, 4, 5]
# sample_nums = random.sample(nums, 3)
# print(sample_nums) # 2, 5, 1

# Task 1:
# Below import codecademylib3_seaborn, import pyplot from the module matplotlib with the alias plt.

# Task 2:
# Import random below the other import statements. It’s best to keep all imports at the top of your file.

import codecademylib3_seaborn
import matplotlib
from matplotlib import pyplot as plt
import random


# Add your code below:

# Task 3
# Create a variable numbers_a and set it equal to the range of numbers 1 through 12 (inclusive).
# numbers_a = range(1,13)

# Task 4
# Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000).

# Feel free to print numbers_b to see your random sample of numbers.

numbers_b = random.sample(range(1000), 12)

print(numbers_b)

# Task 5
# Now let’s plot these number sets against each other using plt. Call plt.plot() with your two variables as its arguments.

plt.plot(numbers_a,numbers_b)


# Task 6
# Now call plt.show() and run your code!

# You should see a graph of random numbers displayed. You’ve used two Python modules to accomplish this (random and matplotlib).

plt.show()