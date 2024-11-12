# Task 6: IND-CCA security
from utils import input_int, print_hr # Import helper functions from utils
from nt375_task1 import expo # Import the expo module from task1
from nt375_task4 import modular_inverse # Import the multiplication inverse function

# Function to calculate the modified ciphertext c′ and the modular inverse of 2 mod N and return them
def find_modified_c_and_inverse_of_2 (c: int, e: int, N: int) -> tuple[int, int]:
  # Calculate the modified ciphertext c′ = (2^e * c) mod N
  modified_c = (expo(2, e, N) * c) % N
  print(f"The modified ciphertext c′ is = {modified_c}")

  # Calculate the modular inverse of 2 mod N
  inverse_of_2 = modular_inverse(2, N)
  print(f"The inverse of 2 mod {N} is = {inverse_of_2}")

  print_hr() # print break line
  return modified_c, inverse_of_2


# Function to decrypt the modified ciphertext c′ using the modular inverse of 2 to get the original message (m)
def modified_decryption(N: int, inverse_of_2: int, modified_m: int = None):
  print("Please decrypt the modified ciphertext c′ using your program from Task 4.")
  if modified_m is None:
    modified_m = input_int("Please input the plaintext m′ decrypted from c′: ")

  # Calculate the original plaintext message m = (m′ * inverse_of_2) mod N
  m = (modified_m * inverse_of_2) % N
  print(f"The original plaintext message m computed from m′ is: {m}")
  print_hr() # print break line


# Main function to run the program and perform the modified decryption operation
if __name__ == "__main__":
  # Receive the inputs N and e from task 4
  N = input_int("Please enter the public parameter N: ")
  e = input_int("Please enter the encryption exponent e: ")
  print_hr() # print break line

  # Receive the ciphertext c from task 4
  c = input_int("Please enter the ciphertext c: ")
  print_hr() # print break line

  # Find the modified ciphertext c′ and the modular inverse of 2
  modified_c, inverse_of_2 = find_modified_c_and_inverse_of_2(c, e, N)

  # Decrypt the ciphertext from the modified message, computing from the modified ciphertext
  modified_decryption(N, inverse_of_2)
