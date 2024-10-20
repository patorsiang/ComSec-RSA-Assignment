from utils import input_int, print_hr # Import helper functions from utils

# Function implementing the Extended Euclidean algorithm (EEA)
# It receives 2 integers, a and b, and return 3 numbers, r1, s1, and t1
# for computing GCD (greatest common divisor) of a and b
# gcd(a, b) = ax + by -> r1 = gcd(a, b), s1 = x, t1 = y
def EEA(a: int, b: int) -> tuple[int, int, int]:
  print_hr()  # print break line

  # Initialize the values for (r1, s1, t1) and (r, s, t)
  print("The values of (r,s,t) in the steps of EEA are:")
  r1 = a
  s1 = 1
  t1 = 0
  r = b
  s = 0
  t = 1

  # Perform the Extended Euclidean algorithm until r becomes 0
  while r != 0:
    # Update the values for r1, s1, t1 based on the previous values and quotient
    q = r1 // r # Calculate quotient (integer division)
    r1, r = r, r1 - q * r
    s1, s = s, s1 - q * s
    t1, t = t, t1 - q * t

    # Print a step of the algorithm
    print(f"({r}, {s}, {t})")

  # Return the final values of r1 (g), s1(x), and t1(y)
  return r1, s1, t1

# Function to show the final answer following the format
def output (g: int, x: int, y: int):
  print_hr()  # print break line
  print(f'The values of (g,x,y) are: ({g}, {x}, {y})')
  print_hr()  # print break line

if __name__ == "__main__":
  # taking a and b as integers
  a = input_int("Please enter a: ")
  b = input_int("Please enter b: ")

  # calling the EEA function with a and b and printing the result
  g, x, y = EEA(a,b)
  output(g, x, y)
