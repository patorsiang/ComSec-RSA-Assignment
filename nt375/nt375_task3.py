def is_prime (n: int) -> tuple[bool, int]:
  if n <= 1:
    return False, None
  start_num = 2
  end_num = int(n**0.5) + 1
  for i in range(start_num, end_num):
    if n % i == 0:
      return False, i
  return True, None

def find_a_prime_num (n: int) -> tuple[str]:
  start_num = 2 ** (n-1)
  end_num = 2 ** (n)

  for i in range(start_num, end_num):
    is_prime_result, _ = is_prime(i)
    if is_prime_result:
      return i

def output (n, p):
  print("--------------------------------")
  print(f"The {n}-bit prime is p = {p}")
  print("--------------------------------")

if __name__ == "__main__":
  n = input("Please enter the parameter n: ")
  prime_num = find_a_prime_num(n)
  output(n, prime_num)
