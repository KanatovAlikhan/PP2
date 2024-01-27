'''
#Ex1
def gram_to_ounces(grams):
    print(grams/28.3495231)
gram_to_ounces(int(input("Write grams ")))
#Ex2
def conversion(F):
    print("C=",(5/9)*(F-32))
conversion(int(input("Write F ")))
#Ex3
def solve(numheads, numlegs):
    print("The Chickens= ", numheads-(numlegs-numheads*2)//2,'\n' , "The Rabbits= ", (numlegs-numheads*2)//2)
solve(int(input("Write heads ")) , int(input("Write legs ")))
#Ex4 
def filter_prime(primes):
    for x in primes:
        print("Primes=",x," ")
n=int(input("Write length "))
mylist=list()
myprimes=list()
while n>0:
    a=int(input())
    mylist.append(a)
    n-=1
for i in mylist:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        myprimes.append(i)
filter_prime(myprimes)
#Ex9
import math
def volume(r):
    ans=4/3 * 3.14 * math.pow(r,3)
    print(ans)
volume(int(input("Write radius ")))
#Ex11
def palindrome(word):
    if(word == t):
        print("Word is palindrome")
    else:
        print("Word is not palindrome")
s=str(input("Write word "))
t=str()
mylist=list()
for x in s:
    mylist.append(x)
mylist.reverse()
for x in mylist:
    t+=x
palindrome(s)
'''