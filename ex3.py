import math
n=int(input())
m=int(input())
s1=s2=0
for i in range(1,m+1):
    if i%n==0:
        s1+=i
    else:
        s2+=i
print(abs(s1-s2))
        