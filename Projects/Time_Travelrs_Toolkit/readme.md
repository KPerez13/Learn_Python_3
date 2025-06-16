# Time Traveler's Toolkit

This project simulates a time travel experience using various Python modules, covering essential programming concepts like custom modules, date/time handling, precise financial calculations, and random selections.


## Project Goal

The aim was to create a Python script (`time_travelers_toolkit.py`) that would:
* Define a custom function to generate a time travel message.
* Utilize the **`datetime` module** to get the current year.
* Employ the **`decimal` module** for accurate cost calculation.
* Use the **`random` module`** to pick a random target year and destination.
* Combine all these elements to produce a personalized time travel itinerary and cost.


## How to Run the Project

1.  Ensure both `custom_module.py` and `time_travelers_toolkit.py` are in the same directory.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the files.
4.  Run the main script using:
    ```bash
    python time_travelers_toolkit.py
    ```
5.  Observe the output, which will show the current date/time (for reference) and your personalized time travel message.


## Code Overview

### `custom_module.py`

This file defines a simple function responsible for formatting the final time travel message.

```python
# custom_module.py
def generate_time_travel_message(year, destination, cost):
  """
  Generates a formatted string for the time travel message.

  Args:
    year (int): The target year for time travel.
    destination (str): The chosen destination for time travel.
    cost (str): The formatted cost of the time travel (e.g., "$12345.67").

  Returns:
    str: The complete time travel message.
  """
  return f"Pack your bags! You're traveling to {destination} in the year {year}. The cost of this trip will be ${cost}."
```

### `time_travelers_toolkit.py`

This is the main script that brings all the pieces together.

```python
# time_travelers_toolkit.py
import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message # Key: Import the specific function directly

# 1. Get Today's Date
now = dt.datetime.now()
print(f"Current Date and Time: {now}") # Prints current date/time for reference

# 2. Calculate the Time Travel Cost
base_cost = Decimal(13000) # Base cost as a Decimal object for precision

current_year = now.year # Get current year from the datetime object

# 3. Random Selections
random_year = randint(2010, 3140) # Generate a random target year
possible_destinations = ['Mexico', 'Colombia', 'United States', 'Japan', 'France', 'Italy']
final_destination = choice(possible_destinations) # Randomly select a destination from the list

# Calculate difference in years (absolute value ensures it's always positive)
difference_in_year = abs(random_year - current_year)

# Determine cost multiplier (example logic: 1.0 plus 0.1 for each year of difference)
cost_multiplier = 1.0 + (difference_in_year * 0.1)

# Crucial: Convert the float cost_multiplier to a Decimal for compatible multiplication
# Using str() is often safer for float-to-Decimal conversion to maintain precision
cost_multipler_decimal = Decimal(str(cost_multiplier))

# Calculate final cost by multiplying two Decimal objects
final_cost = base_cost * cost_multipler_decimal

# Format final cost to two decimal places for display in the message
formatted_final_cost = f"{final_cost:.2f}"

# 4. Using the Custom Module
# Call the custom function with all calculated arguments and print the returned message
print(generate_time_travel_message(random_year, final_destination, formatted_final_cost))
```



## Key Learning Points & Debugging Journey

This project, while seemingly straightforward, presented several common challenges that are excellent learning opportunities:

### 1. Module Imports and Aliases (`import module as alias`, `from module import func`)
* **Initial Challenge:** Confusion often arose between importing an entire module (e.g., `import module`) which requires prefixing functions (`module.function()`), and importing specific functions directly (`from module import function`) which allows direct calls (`function()`). Errors like `NameError` or incorrect syntax (`import function from module`) were common.
* **Resolution:** We clarified that **`import module as alias`** is great for `datetime` where you use multiple components (e.g., `dt.datetime`, `dt.date`), and **`from module import func1, func2`** is perfect when you only need specific functions (e.g., `randint`, `choice`). The final fix for the `NameError` with `generate_time_travel_message` involved explicitly importing it as `from custom_module import generate_time_travel_message`.

### 2. Accessing Object Attributes vs. Calling Methods (`object.attribute` vs. `object.method()`)
* **Initial Challenge:** Attempting to get the year from a `datetime` object using `now.year()` (with parentheses), treating an attribute like a method.
* **Resolution:** We learned that **attributes** (data stored directly on an object, like `now.year`) are accessed directly using dot notation, while **methods** (functions that perform actions or return calculated values, like `dt.datetime.now()`) are called with parentheses.

### 3. Using `abs()` for Absolute Difference
* **Initial Challenge:** Calculating year differences could result in negative numbers if traveling to the past, which wasn't suitable for a "cost" metric. Misplacing `abs()` (e.g., `abs(var) = ...`) or applying it to individual numbers before subtraction also occurred.
* **Resolution:** The **`abs()`** built-in function is used to get the **absolute value** (distance from zero). The correct approach was to apply `abs()` to the *result* of the subtraction: `abs(target_year - current_year)`.

### 4. `Decimal` Type for Financial Precision
* **Initial Challenge:** A significant `TypeError: unsupported operand type(s) for *: 'decimal.Decimal' and 'float'` arose when multiplying `base_cost` (a `Decimal`) by `cost_multiplier` (a `float`). Direct conversion to `int()` was considered but would lead to loss of precision.
* **Resolution:** The **`decimal` module** is designed for exact precision in financial calculations. To prevent `TypeError` and maintain accuracy, we explicitly converted the `float` `cost_multiplier` to a `Decimal` object using **`Decimal(str(cost_multiplier))`** before performing the multiplication. This ensures all parts of the calculation adhere to `Decimal`'s high precision standards.

### 5. Order of Operations / Variable Definition
* **Initial Challenge:** A `NameError` occurred because a variable (`random_year`) was used in a calculation *before* the line defining that variable was executed in the script. Python reads and executes code sequentially.
* **Resolution:** We reinforced the fundamental rule that **variables must be defined before they are used**. Moving the definition of `random_year` to an earlier point in the script, before its use in calculating `difference_in_year`, resolved this `NameError`.

### 6. `print()` vs. `return` in Functions
* **Initial Challenge:** The `custom_module` function used `print()` to display the message but didn't explicitly `return` anything. This led to `None` being printed in the main script (because `print()` was trying to show the function's implicit `None` return value). Additionally, the f-string inside the function was missing its `f` prefix, preventing variable values from being inserted.
* **Resolution:** We clarified that functions should **`return`** values if those values are to be used by other parts of the program, while `print()` is for displaying output directly to the console. The final solution involved changing the function to `return f"..."` so that the main script could then `print()` the actual formatted message.

---

This project was a fantastic exercise in integrating different Python modules and tackling common programming challenges. The process of debugging these errors provided a deeper understanding of Python's data types, variable scope, and function behavior.