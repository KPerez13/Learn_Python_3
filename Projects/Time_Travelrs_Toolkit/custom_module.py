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
