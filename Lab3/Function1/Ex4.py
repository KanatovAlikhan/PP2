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