#Ex1
n=int(input())
a=0
mylist=list()
ans=1
for i in range(n):
    a=int(input())
    mylist.append(a)
x=iter(mylist)
for i in range(n):
    ans*=next(x)
print(ans)
#Ex2
s=input()
x=iter(s)
upper=0
lower=0
for i in x:
    if i>="A" and i<="Z":
        upper+=1
    else:
        lower+=1
print("Upper =",upper)
print("Lower =",lower)
#Ex3
s=input()
t=s
x=iter(t)
ans=True
for i in s[::-1]:
    if i!=next(x):
        ans=False
        break
print(ans)
#Ex4
import math
import time
number=int(input("Write a number "))
milisecond=int(input("Write a milisecond "))
seconds=milisecond/1000
time.sleep(seconds)
print(math.sqrt(number))
#Ex5
n=int(input())
mylist=list()
for i in range(n):
    a=input()
    if a=="true" or a=="True":
        mylist.append(True)
    else:
        mylist.append(False)
mytuple=tuple(mylist)
x=all(mytuple)
print(x)
