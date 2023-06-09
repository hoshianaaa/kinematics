import math

# 0.0000000001 以下の数値を0とする

def deg2rad(angle):
  return math.radians(angle)

def zero(value):
  if value < 0.0000000000001:
    return 0
  else:
    return value

def cos(angle):
  output = zero(math.cos(deg2rad(angle)))
  return output

def sin(angle):
  output = zero(math.sin(deg2rad(angle)))
  return output

def atan2(y,x):
  output = math.atan2(y,x)
  return output

# 円周を計算, d: 直径
def circumference(d):
  return d * math.pi

arc_angle_description = "arc_angle(d,l) : 直径dの円周上を,lだけ移動した際の始点と終点のなす角度を計算"
def arc_angle(d, l):
  output = l / circumference(d) * 360
  return output

arc_angle2_description = "arc_angle2(d,angle) : 直径d, 角度angle分の円周長"
def arc_angle2(d, angle):
  output = circumference(d) * angle / 360
  return output

arc_angle3_description = "arc_angle3(l,angle) : 円周長 l を角度 angle で生成できる円弧直径 dを求める"
def arc_angle3(l, angle):
  d = l * 360 / angle / math.pi
  return d

triangle_bottom_description = "頂角の角度、底辺の値から2等辺三角形の斜辺を求める"
def triangle_bottom(angle, bottom):
#  l * sin(angle/2) = bottom / 2  
  l = bottom / 2 / sin(angle/2)
  return l

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
    
    print("atan2(" + str(y) + "," + str(x) + ")" , ":" ,atan2(y, x))

  print()
  d_list = [1,2,3,4,5,10]
  for d in d_list:
    print("circumference(" + str(d) + ")" , ":" ,circumference(d))

  print()
  print(arc_angle_description)

  d = 2
  l = 1

  print("arc_angle(" + str(d) + "," + str(l) + ")" + " : " + str(arc_angle(d,l)) + " (deg)")

  print()
  print(arc_angle2_description)

  d = 2
  angle = 90

  print("arc_angle2(" + str(d) + "," + str(angle) + ")" + " : " + str(arc_angle2(d,angle)))

  print()
  print(arc_angle3_description)

  l = 2.5
  angle = 90

  print("arc_angle3(" + str(l) + "," + str(angle) + ")" + " : " + str(arc_angle3(l,angle)))

  print(triangle_bottom_description)
  angle = 90
  bottom = 2.5 
  print("angle:", angle)
  print("bottom:", bottom)
  print(triangle_bottom(angle, bottom))
  print("```")
 


