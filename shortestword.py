a="My name i v harshitha h reddy"
d=a.split()
min=d[0]
c=[]
for i in d[1:]:
    if(len(i)==len(min)):
        c.append(i)
    if(len(i)<len(min)):
        min=i
print(min,end=' ')
print(' '.join(c))
