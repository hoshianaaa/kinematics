import math

def cos(angle):
  output = math.cos(math.radians(angle))
  return output

if __name__ ==  "__main__":

  angle_list = [30,60,90]
  for angle in angle_list:
    f = "cos(" + str(angle) + ")"
    print(f, ",", eval(f))
