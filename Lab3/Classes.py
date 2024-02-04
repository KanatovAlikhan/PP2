#Ex1
class first():
    def __init__(self,name):
        self.name=name
    def getString(self):
        self.name=name
    def printString(self):
        print(self.name.upper())
Name=first(input("Write your name ))
Name.printString()
#Ex2
class Shape():
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        print(self.length*self.length)
leng=Square(int(input("Write the length ")))
leng.area()
#Ex3
class Shape():
    def __init__(self,length,width):
        self.length=length
        self.width=width
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print(self.length*self.width)
atribute=Rectangle(int(input("Length ")),int(input("Width ")))
atribute.area()
#Ex4
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"x={self.x} and y={self.y}")
    def move(self, nx, ny):
        self.x = nx
        self.y = ny

    def dist(self, ot):
        dist_x = self.x - ot.x
        dist_y = self.y - ot.y
        distance = math.sqrt(dist_x**2 + dist_y**2)
        return distance
point1 = Point(int(input()),int(input()))
point2 = Point(int(input()),int(input()))
point1.show()
point2.show()
print("Distance=",point1.dist(point2))
point2.move(int(input()),int(input()))
point2.show()
#Ex5
class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,money):
        self.balance+=money
        print("Hello,",self.owner,"!","Your balance is",self.balance)
    def withdraw(self,minus_money):
        if self.balance>=minus_money:
            self.balance-=minus_money
            print("Your balace is",self.balance) 
        else:
            print("You have not enough money(((")


acc=Account(input("What is your name "))
acc.deposit(int(input("How much money send to you? ")))
acc.withdraw(int(input("How much do you want to transfer ")))
#EX6
class Prime():
    def __init__(self,mylist):
        self.mylist=mylist
    def filter(self):
        myprimes=[]
        for i in self.mylist:
            c=0
            for j in range(1,i):
                if i%j==0:
                    c+=1
            if c==1:
                myprimes.append(i)
        size=lambda a:a+len(myprimes)
        print(myprimes,"The size of myprimes=",size(0))
numbers=Prime([1,2,3,4,5,6,7,8,9])
numbers.filter()