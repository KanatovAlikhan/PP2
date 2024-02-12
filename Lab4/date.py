#Ex1
import datetime
print(datetime.datetime.now()-datetime.timedelta(days=5))
#Ex2
import datetime
print("Yesterday was",datetime.datetime.today()-datetime.timedelta(days=1))
print("Today is",datetime.datetime.today())
print("Tomorrow will be",datetime.datetime.today()+datetime.timedelta(days=1))
#Ex3
import datetime
now=datetime.datetime.now()
now=now.replace(microsecond=0)
print(now)
#Ex4
import datetime
today=datetime.datetime.now()
few_days=int(input())
some_days_ago=today.replace(day=few_days)
arasi=today.day - some_days_ago.day
print(arasi)
print(arasi*24*60*60)