import random
from utils import input_int

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    start_num = 2
    end_num = int(n ** 0.5) + 1  # You can directly cast to int for square root
    for i in range(start_num, end_num):
        if n % i == 0:
            return False
    return True

def primes_arr_between_1_and_100():
    primes = []
    for num in range(2, 101):
        if is_prime(num):
            primes.append(num)
    return primes

primes_arr = primes_arr_between_1_and_100()

def is_prime_by_partial_trials_division(n: int) -> bool:
  for i in primes_arr:
    if n % i == 0 and i != n:
      return False
  return True

def is_prime_by_fermat_primality_test(n: int, k: int = 50) -> bool:
  for _ in range(k):
    a = random.randint(2, n - 1)
    if (a ** (n-1)) % n != 1:
      return False
  return True

def is_prime_2_step (n: int, k: int = 50) -> bool:
  if not is_prime_by_partial_trials_division(n):
    return False

  return is_prime_by_fermat_primality_test(n, k)

def find_a_prime_num (n: int) -> int:
  start_num = 2 ** (n-1)
  end_num = 2 ** (n)

  for i in range(start_num, end_num):
    if is_prime_2_step(i):
      return i

def output(n: int, p: int):
  print("--------------------------------")
  print(f"The {n}-bit prime is p = {p}")
  print("--------------------------------")

if __name__ == "__main__":
  n = input_int("Please enter the parameter n: ")
  prime_num = find_a_prime_num(n)
  output(n, prime_num)
