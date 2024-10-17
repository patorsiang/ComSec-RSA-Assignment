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
  print("-------------------------------------")
  print(f"The value of m ∧ e mode N is {ans}")
  print("-------------------------------------")

if __name__ == "__main__":
  m = input("Please enter m: ")
  e = input("Please enter e: ")
  N = input("Please enter N: ")

  output(expo(m, e, N))
