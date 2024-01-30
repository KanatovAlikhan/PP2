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
#Ex 5 
import itertools
def perm():
    for x in permutations:
        print(x)
s=str(input())
permutations = list(itertools.permutations(s))
perm()
'''
#Ex6////////////
''' 
s=str(input())
#Ex7
def has_33(nums):
    ans=False
    size=len(nums)
    for i in range(size):
        if nums[i]==3 and nums[i+1]==3:
            ans=True
            break
    print(ans)
has_33([1, 3, 3])
'''
#Ex8////////////////// 

'''
#Ex9
import math
def volume(r):
    ans=4/3 * 3.14 * math.pow(r,3)
    print(ans)
volume(int(input("Write radius ")))
'''
#Ex10///////////
'''
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
#Ex12
def histogram(nums):
    for i in nums:
        print("*"*i)
histogram([4, 9, 7])
#Ex13
import random
def guess():
    print("Hello! What is your name?")
    name=str(input())
    cnt=0
    print("Well,",name,", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    number=random.randint(1, 20)
    a=int(input())
    while number!=a:
        if a>number:
            print("Your guess is too high.")
            print("Take a guess.")
        else:
            print("Your guess is too low.")
            print("Take a guess.")
        a=int(input())
        cnt+=1
    print("Good job,",name,"! You guessed my number in",cnt+1,"guesses!")
guess()
'''