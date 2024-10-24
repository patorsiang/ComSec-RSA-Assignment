# Task 2: Extended Euclidean algorithm (EEA).
from utils import input_int, print_hr # Import helper functions from utils

# Function implementing the Extended Euclidean algorithm (EEA)
# It receives two integers, a and b, and returns three numbers, r1, s1, and t1
# for computing the GCD (greatest common divisor) of a and b
# gcd(a, b) = ax + by -> r1 = gcd(a, b), s1 = x, t1 = y
def EEA(a: int, b: int, wantedPrint: bool = True) -> tuple[int, int, int]:
  # Initialization step for r1, s1, t1, r, s, and t
  r1 = a # Initial r1  equal to a
  s1 = 1 # Initial s1 equal to 1
  t1 = 0 # Initial t1 equal to 0
  r = b # Initial r equal to b
  s = 0 # Initial s equal to 0
  t = 1 # Initial t equal to 1

  # Perform the Extended Euclidean algorithm until r becomes 0
  while r != 0:
    # Update the values for r1, s1, and t1 based on the previous values and quotient following the pseudo-code
    q = r1 // r # Calculate quotient (integer division)
    r1, r = r, r1 - q * r
    s1, s = s, s1 - q * s
    t1, t = t, t1 - q * t

    # The part of a display or print a step; Note: other tasks call this function, so if others do not want it, it needs to hide
    if wantedPrint:
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

  print_hr()  # print break line

  # Initialize the values for (r1, s1, t1) and (r, s, t)
  print("The values of (r,s,t) in the steps of EEA are:")
  # calling the EEA function with a and b and printing the result
  g, x, y = EEA(a,b)
  output(g, x, y)
