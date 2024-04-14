n=int(input())
a=[]

for i in range(n):
    a.append(int(input()))
m=min(a)
a.remove(m)

print(a)
print(min(a))
