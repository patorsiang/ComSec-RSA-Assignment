from utils import input_int, print_hr
from nt375_task1 import expo
from nt375_task4 import multiplication_inverse

def find_modified_c_and_inverse_of_2 (c: int, e: int, N: int) -> tuple[int, int]:
  modified_c = (expo(2, e, N) * c) % N
  print(f"The modified ciphertext c′ is = {modified_c}")
  inverse_of_2 = multiplication_inverse(2, N)
  print(f"The inverse of 2 mode {N} is = {inverse_of_2}")
  print_hr()
  return modified_c, inverse_of_2

def modified_decryption(N: int, inverse_of_2: int, modified_m: int = None):
  print("Please decrypt the modified ciphertext c′ using your program from Task 4.")
  if modified_m is None:
    modified_m = input_int("Please input the plaintext m′ decrypted from c′: ")
  m = (modified_m * inverse_of_2) % N
  print(f"The original plaintext message m computed from m′ is: {m}")
  print_hr()

if __name__ == "__main__":
  N = input_int("Please enter the public parameter N: ")
  e = input_int("Please enter the encryption exponent e: ")
  print_hr()

  c = input_int("Please enter the ciphertext c: ")
  print_hr()

  modified_c, inverse_of_2 = find_modified_c_and_inverse_of_2(c, e, N)

  modified_decryption(N, inverse_of_2)
