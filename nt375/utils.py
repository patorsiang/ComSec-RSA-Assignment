# Function to ensure the input is an integer
def input_int(label: str, min: int = None) -> int:
  while True:
    try:
      value = int(input(label))
      if min is not None:
        if value >= min:
          return value
        else:
          # Error message for input less than the specified number
          print(f"Invalid input. Please enter value more than or equal to {min}")
      else:
        return value  # Return the value if it is an integer
    except ValueError:
      # If the input is not an integer, then show the error message and require the user to enter; otherwise
      print("Invalid input. Please enter an integer.")

# Function to print a horizontal line for separation of output
def print_hr():
  print("--------------------------------")
