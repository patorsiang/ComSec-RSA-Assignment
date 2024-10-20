def input_int(label: str) -> int:
  while True:
    try:
      return int(input(label))
    except ValueError:
      print("Invalid input. Please enter an integer.")


def print_hr():
  print("--------------------------------")
