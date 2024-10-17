def floor (x: int) -> int:
  if x >= 0:
    return int(x)
  else:
    return int(x) - 1 if x != int(x) else int(x)

def EEA(a: int, b: int) -> tuple[int, int, int]:
  print("--------------------------------")
  print("The values of (r,s,t) in the steps of EEA are:")
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
    print(f"({r}, {s}, {t})")

  return r1, s1, t1

def output (g: int, x: int, y: int):
  print("--------------------------------")
  print(f'The values of (g,x,y) are: ({g}, {x}, {y})')
  print("--------------------------------")

if __name__ == "__main__":
  a = input("Please enter a: ")
  b = input("Please enter b: ")

  g, x, y = EEA(a,b)
  output(g, x, y)
