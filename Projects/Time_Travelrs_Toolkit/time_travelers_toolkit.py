# time_travelers_toolkit.py
import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message # Key: Import the specific function

# 1. Get Today's Date
now = dt.datetime.now()
print(f"Current Date and Time: {now}") # Added f-string for clarity on output

# 2. Calculate the Time Travel Cost
base_cost = Decimal(13000) # Base cost as a Decimal object

current_year = now.year # Get current year

# 3. Random Selections
random_year = randint(2010, 3140) # Generate a random target year
possible_destinations = ['Mexico', 'Colombia', 'United States', 'Japan', 'France', 'Italy']
final_destination = choice(possible_destinations) # Randomly select a destination

difference_in_year = abs(random_year - current_year) # Calculate absolute difference in years

cost_multiplier = 1.0 + (difference_in_year * 0.1) # Determine cost multiplier (example logic)

# Crucial for Decimal type compatibility
cost_multipler_decimal = Decimal(str(cost_multiplier)) # Convert float multiplier to Decimal (using str for precision)

final_cost = base_cost * cost_multipler_decimal # Calculate final cost with Decimal precision
formatted_final_cost = f"{final_cost:.2f}" # Format final cost to two decimal places for display

# 4. Using the Custom Module
# Call the custom function and print the generated message
print(generate_time_travel_message(random_year, final_destination, formatted_final_cost))
