import re
#Ex1
txt=input()
x=re.search("ab*",txt)
print(x)
#Ex2
txt=input()
x=re.search(r"ab{2,3}",txt)
print(x)
#Ex3
txt=input()
x=re.findall(r"[a-z_]+_[a-z]+",txt)
print(x)
#Ex4
txt=input()
x=re.findall(r"[A-Z][a-z]+",txt)
print(x)
#Ex5
txt=input()
x=re.findall(r".*a.*b$",txt)
print(x)
#Ex6
txt=input()
x=re.sub(r"[., ]",":",txt)
print(x)
#Ex7
txt=input()
x=re.sub(r"[_]","",txt)
print(x)
#Ex8
txt=input()
x=re.findall(r"[^A-Z]*[A-Z][^A-Z]*",txt)
result=' '.join(x)
print(result)
#Ex9
txt=input()
x=re.findall(r"[A-Z][^A-Z]*",txt)
res=' '.join(x)
print(res)
#Ex10
txt=input()
x=re.sub(r"(?<!^)(?=[A-Z])","_",txt).lower()
print(x)