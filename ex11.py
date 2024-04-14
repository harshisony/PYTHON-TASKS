a,b,c,d=map(int,input().split())
l=[]
o=[]
k=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
d=list(set(l))
for i in l:
    if i not in k:
        k.append(i)
    else:
        o.append(i)
o=list(set(o))
for i in o:
    d.remove(i)
s=sum(d)
s2=sum(o)
print(s-s2)
        
        
        
