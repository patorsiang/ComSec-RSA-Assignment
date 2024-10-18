def input_int(label: str) -> int:
  try:
    return int(input(label))
  except ValueError:
      print("Invalid input. Please enter an integer.")
