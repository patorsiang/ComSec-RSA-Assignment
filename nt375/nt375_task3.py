# Task 3: Finding a prime number.
import random # Import the random module for generating random numbers
from nt375_task1 import expo # Import the expo module from task1
from utils import input_int, print_hr # Import helper functions from utils

# Function to check prime numbers for small numbers
def is_prime(n: int) -> bool:
  if n <= 1:
    return False
  start_num = 2
  end_num = int(n ** 0.5) + 1  # You can directly cast to int for square root
  # Check if it is a number composite or not between 2 and the square root of the number
  for i in range(start_num, end_num):
    if n % i == 0:
      return False
  return True

# Function to generate prime numbers array including numbers between 0 and 100
def primes_arr_between_1_and_100():
    primes = []
    for num in range(2, 101): # 2 is the first prime number as all knows about it, so starting from 2 until 101
        if is_prime(num):
            primes.append(num) # if it is a prime number, add to the array
    return primes # return prime numbers array

# Global variables
# prime numbers array including prime numbers between 0 and 100
primes_arr = primes_arr_between_1_and_100()

# Function to check number: is it prime or not by number in prime numbers array can or cannot be a divisor of the number
def is_prime_by_partial_trials_division(n: int) -> bool:
  for i in primes_arr:
    if n % i == 0 and i != n:
      return False
  return True

# Function to check number: it is prime or not by using Fermat's primality testing algorithm
def is_prime_by_fermat_primality_test(n: int, k: int = 50) -> bool:
  for _ in range(k): # check for k times
    a = random.randint(2, n - 1) # random number
    if expo(a, n-1, n) != 1: # if a is not prime a^(n-1) mod n doesn't equal 1
      return False
  # If n passes all tests, it is (probably) prime
  return True

# check prime numbers following two steps
def is_prime_2_step (n: int, k: int = 50) -> bool:
  # step1: check between 0 and 100 can be a partial divisor
  if not is_prime_by_partial_trials_division(n):
    return False # if there is a partial divisor, it is (probably) prime

  # step2: Check Fermat's primality testing algorithm to confirm if it is prime, in the condition that it passes step 1
  return is_prime_by_fermat_primality_test(n, k)


# Function to find first prime number between 2^(n-1) and 2^(n) - 1.
def find_a_prime_num (n: int) -> int:
  start_num = 2 ** (n-1)
  end_num = 2 ** (n)

  for i in range(start_num, end_num):
    if is_prime_2_step(i):
      return i

# Function to show the final output following the format
def output(n: int, p: int):
  print_hr() # print break line
  print(f"The n-bit prime is p = {p}")
  print_hr() # print break line

if __name__ == "__main__":
  # Taking a parameter n, the input should be equal to or greater than 3; limit it because the look will crash
  n = input_int("Please enter the parameter n: ", 3)
  # finding the first prime number between 2^(n-1) and 2^(n)
  prime_num = find_a_prime_num(n)
  # printing the result in the required format
  output(n, prime_num)
