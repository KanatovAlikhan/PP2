def likeset(elements):
    cntlist=list()
    for i in range(0,10):
        cntlist.append(0)
    for i in elements:
        cntlist[i]+=1
    cnt=0
    for i in cntlist:
        if i>=1:
            mylist2.append(cnt)
        cnt+=1
    print(mylist2)
x=int(input())
mylist=list()
while(x>0):
    a=int(input())
    mylist.append(a)
    x-=1
mylist2=list()

likeset(mylist)