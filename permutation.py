import math

a=input()
l=len(a)
b=list(a)
count=0
d={}
c=1
for i in a:
    d[i]=d.get(i,0)+1
for i in d.values():
    if i>1:
        c=c*math.factorial(i)
n=math.factorial(l)
res=n/c
print(res)

