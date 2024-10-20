import random
from utils import input_int, print_hr
from nt375_task3 import is_prime_2_step
from nt375_task1 import expo

def gcd (a, b):
  if b > a:
    a, b = b, a

  while b != 0:
    a, b = b, a % b
  return a

def EEA(a: int, b: int) -> tuple[int, int, int]:
  r1 = a
  s1 = 1
  t1 = 0
  r = b
  s = 0
  t = 1

  while r != 0:
    q = r1 // r
    r1, r = r, r1 - q * r
    s1, s = s, s1 - q * s
    t1, t = t, t1 - q * t

  return r1, s1, t1

def generate_prime(n: int) -> int:
    while True:
        p = random.randint(2**(n-1), 2**n - 1)
        if is_prime_2_step(p):
            return p

def multiplication_inverse(e: int, M: int) -> int:
    g, x, _ = EEA(e, M)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % M

def setup(v: int) -> tuple[int, int]:
  p = generate_prime(v//2)
  q = generate_prime(v//2)
  N = p * q

  M = (p - 1) * (q - 1)
  e = random.randint(2, M - 1)
  while gcd(e, M) != 1:
    e = random.randint(2, M - 1)

  d = multiplication_inverse(e, M)

  return p, q, N, e, d

def print_setup (p: int, q: int, N: int, e: int, d: int):
  print_hr()
  print("Setup: ")
  print(f"The first prime generated by the Setup algorithm is p = {p}")
  print(f"The second prime generated by the Setup algorithm is q = {q}")
  print(f"The integer N = pq = {N}")
  print(f"The encryption exponent is e = {e}")
  print(f"The decryption exponent is d = {d}")

def input_option () -> int:
  print_hr()
  print("Options: ")
  print("1. Encryption")
  print("2. Decryption")
  print("Any other number to quit")
  option = input_int("Your options: ")
  return option

def encryption(N: int, e: int, m: int = None) -> int:
  print_hr()
  print("Encryption:")
  print(f"Your message space is the set {{Z/NZ}} = {{0, 1, ..., {N-1}}}")
  c = None
  if m is None:
    m = input_int("Please enter a number from this set: ")
  if 0 <= m < N:
    c = expo(m, e, N)
    print(f"The ciphertext for your message {m} is {c}")
  else:
    print(f"Invalid message! Please enter a number between 0 and {N-1}.")
  return c

def decryption(N: int, d: int, c: int = None) -> int:
  print_hr()
  print("Decryption:")
  print(f"Your ciphertext space is the set {{Z/NZ}} = {{0, 1, ..., {N-1}}}")
  m = None
  if c is None:
    c = input_int("Please enter a number from this set: ")
  if 0 <= c < N:
    m = expo(c, d, N)
    print(f"The plaintext for your ciphertext {c} is {m}")
  else:
    print(f"Invalid ciphertext! Please enter a number between 0 and {N-1}.")
  return m

def main():
  nu = input_int("Please enter the security parameter 'nu': ")

  p, q, N, e, d = setup(nu)
  print_setup(p, q, N, e, d)

  while True:
    option = input_option()
    match option:
      case 1:
        encryption(N,e)
      case 2:
        decryption(N,d)
      case _:
        print_hr()
        exit(0)

if __name__ == "__main__":
  main()
