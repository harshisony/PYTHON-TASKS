n=input()[:10]
l=list(n)
s=sorted(l)
o=list(set(s))
print(o)
p=[]
f=[]
for i in range(len(l)):
    f.append(l.count(i))
print(f) 
if(len(n)==0 | n.isalpha()):
    print (0)
else:
    d={}
    j=0
    c=0
    for i in range(0,len(l)):
        d[i]=l[j]
        j+=1
    print(d)
    for i in range(len(l)):
        if(d[i]!=f[i]):
            c=1    
    if c==1:
        print(0)
    else:
        print(len(l)-1)