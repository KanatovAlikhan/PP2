#Ex1
def kvadrat(n):
    for i in range(n+1):
        yield i**2
n=int(input())
x=kvadrat(n)
for i in x:
    print(i)
#Ex2
def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input())
ans=even(n)
for i in ans:
    print(i,end=" ")
#Ex3
def divisible(n):
    for i in range(0,n+1):
        if i%3==0 or i%4==0:
            yield i
n=int(input())
ans=divisible(n)
for i in ans:
    print(i,end=" ")
#Ex4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
ans=squares(int(input()),int(input()))
for i in ans:
    print(i,end=" ")
#Ex5
def fn(n):
    while n>=0:
        yield n
        n-=1
ans=fn(int(input()))
for i in ans:
    print(i,end=" ")