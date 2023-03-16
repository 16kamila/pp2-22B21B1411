import math
#1
deg=int(input("degree: "))
print(math.radians(deg))

#2 - area of trapezoid
h=int(input("height: "))
b1=int(input("base 1: "))
b2=int(input("base 2: "))
print(((b1+b2)/2)*h)

#3 - reg polygon area
n=int(input("sides: "))
l=int(input("lenght: " ))
area = n*(math.pow(l, 2))/(4*math.tan(math.pi/n))
print(int(area))

#4 area of parallelogram
b=int(input("base: "))
h=int(input("height: "))
print(b*h)
