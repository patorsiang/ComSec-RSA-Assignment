from utils import input_int, print_hr

def expo(m: int, e: int, N: int) -> int:
    result = 1
    base = m % N
    while e > 0:
        if e % 2 == 1:
            result = (result * base) % N
        base = (base * base) % N
        e //= 2
    return result

def output(ans: int):
  print_hr()
  print(f"The value of m ∧ e mode N is {ans}")
  print_hr()

if __name__ == "__main__":
  m = input_int("Please enter m: ")
  e = input_int("Please enter e: ")
  N = input_int("Please enter N: ")

  output(expo(m, e, N))
