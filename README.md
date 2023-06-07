
- command

```
$ python3 kinematics
```

- output

```
sin(1 deg) : 0.01745240643728351
sin(5 deg) : 0.08715574274765817
sin(30 deg) : 0.49999999999999994
sin(60 deg) : 0.8660254037844386
sin(90 deg) : 1.0
sin(180 deg) : 0
sin(270 deg) : 0
sin(360 deg) : 0
sin(450 deg) : 1.0

cos(1 deg) : 0.9998476951563913
cos(5 deg) : 0.9961946980917455
cos(30 deg) : 0.8660254037844387
cos(60 deg) : 0.5000000000000001
cos(90 deg) : 0
cos(180 deg) : 0
cos(270 deg) : 0
cos(360 deg) : 1.0
cos(450 deg) : 0

atan2(1,0) : 1.5707963267948966
atan2(1,1) : 0.7853981633974483
atan2(0,1) : 0.0

circumference(1) : 3.141592653589793
circumference(2) : 6.283185307179586
circumference(3) : 9.42477796076938
circumference(4) : 12.566370614359172
circumference(5) : 15.707963267948966
circumference(10) : 31.41592653589793

arc_angle(d,l) : 直径dの円周上を,lだけ移動した際の始点と終点のなす角度を計算
arc_angle(2,1) : 57.29577951308232 (deg)

arc_angle2(d,angle) : 直径d, 角度angle分の円周長
arc_angle2(2,90) : 1.5707963267948966

arc_angle3(l,angle) : 円周長 d を角度 angle で生成できる円弧直径 dを求める
arc_angle3(2.5,90) : 3.183098861837907
```
