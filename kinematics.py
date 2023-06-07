import math

# 0.0000000001 以下の数値を0とする
def zero(value):
  if value < 0.0000000000001:
    return 0
  else:
    return value

def cos(angle):
  output = zero(math.cos(math.radians(angle)))
  return output

def sin(angle):
  output = zero(math.sin(math.radians(angle)))
  return output

def atan2(y,x):
  output = math.atan2(y,x)
  return output

if __name__ ==  "__main__":


  angle_list = [1, 5, 30, 60, 90, 180, 270, 360, 450]

  print()
  print("- command")
  print()
  print("```")
  print("$ python3 kinematics")
  print("```")

  print()
  print("- output")
  print()

  print("```")

  for angle in angle_list:
    print("sin(" + str(angle) + " deg)", ":", sin(angle))

  print()

  for angle in angle_list:
    print("cos(" + str(angle) + " deg)", ":", cos(angle))

  print()

  vec_list = [
    [0,1],
    [1,1],
    [1,0],
  ]

  for vec in vec_list:
    x = vec[0]
    y = vec[1]
    
    print("atan2(" + str(y) + "," + str(x) + ")" ,",",atan2(y, x))

  print("```")

