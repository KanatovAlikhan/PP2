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