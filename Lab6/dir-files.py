import os
#Ex1
ex=input("Write the path to dir ")
folders=os.listdir(ex)
for i in folders:
    print(i,end=" ")
#Ex2
ex=input("Write the path to dir ")
existence=os.path.exists(ex)
if existence==False:
    print("It doesn't exist")
    readability=os.access(ex,os.R_OK)
    print(readability)
    writability=os.access(ex,os.W_OK)
    print(writability)
    executability=os.access(ex,os.X_OK)
    print(executability)
else:
    print("It exists")
    readability=os.access(ex,os.R_OK)
    print(readability)
    writability=os.access(ex,os.W_OK)
    print(writability)
    executability=os.access(ex,os.X_OK)
    print(executability)
#Ex3
ex=input("Write the path to dir ")
if os.path.exists(ex):
    print("It exists")
    print(os.path.basename(ex))
    print(os.path.dirname(ex))
else:
    print("It doesn't exist")
#Ex4
file=open("someText.txt","r")
cnt=0
for i in file:
    cnt+=1
print(cnt)
file.close()
#Ex5
file=open("someText2.txt","w")
n=int(input())
s=0
smm=list()
for i in range(n):
    s=int(input())
    smm.append(s)
file.write(str(smm))
print("check someText2.txt")
file.close()
#Ex6
for i in range(26):
    file=chr(ord('A') + i)+".txt"
    open_file=open(file,"w")
#Ex7
file = open("someText2.txt","r")
file1 = open("someText1.txt","a")
for i in file:
    file1.write(i)
file.close()
file1.close()
#Ex8
ex=input()
if os.path.exists(ex):
    print("Yes exists")
    os.remove(ex)
else:
    print("This path is not correct")
'''
here in ex8 i created file todel.txt 
so you can try it with it or open new 
file and wrie its name.txt'''