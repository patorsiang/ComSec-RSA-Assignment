# Function to ensure the input is an integer
def input_int(label: str) -> int:
  while True:
    try:
      return int(input(label)) # Prompt the user with a label and convert it to an integer
    except ValueError:
      # If the input is not an integer, then show the error message and require the user to enter; otherwise
      print("Invalid input. Please enter an integer.")

# Function to ensure the input is a positive integer
def input_positive_int(label: str) -> int:
    while True:
        value = input_int(label)  # Get the input using input_int function
        if value > 0:
            return value  # Return the value if it is positive
        else:
            # Error message for negative input
            print("Invalid input. Please enter a positive integer.")

# Function to print a horizontal line for separation of output
def print_hr():
  print("--------------------------------")
