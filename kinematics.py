import math

def cos(angle):
  output = math.cos(math.radians(angle))
  return output

if __name__ ==  "__main__":
  f = "cos(30)"
  print(f, eval(f))
  print(eval(f))
