from utils import input_positive_int, print_hr # Import helper functions from utils

# Function to calculate m^e mod N by taking m, e, and N.
def expo(m: int, e: int, N: int) -> int:
    result = 1 # initial value
    base = m % N # step 1: Compute the base modulus N
    while e > 0:
        if e % 2 == 1: # If e is odd, multiply by the current base
            result = (result * base) % N
        base = (base * base) % N # double itself modular N
        e //= 2 # Right shift (divide by 2)
    return result # Return the final result of m^e mod N

# Function to show results following the question output format
def output(ans: int):
  print_hr()  # print break line
  print(f"The value of m ∧ e mode N is {ans}") # print the final answer
  print_hr()  # print break line

if __name__ == "__main__":
  # taking a positive number of arguments, m, e, and N
  m = input_positive_int("Please enter m: ")
  e = input_positive_int("Please enter e: ")
  N = input_positive_int("Please enter N: ")

  # calling the expo function with m, e, and N and printing the result
  output(expo(m, e, N))
