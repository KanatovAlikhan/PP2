#Ex1
import math
n=int(input())
print(math.radians(n))
#Ex2
import math
height=int(input("Height= "))
a=int(input("a= "))
b=int(input("b= "))
print((a+b)*height/2)
#Ex3
import math
sides=int(input("Sides= "))
length=int(input("Length= "))
area=(sides*length**2)/(4*math.tan(math.pi/sides))
print(int(area))
#Ex4
import math
base=float(input("Base= "))
height=float(input("Height= "))
print(base*height)