a=list(map(int,input().split()))
s1=s2=0
l=[]
for i in range(0,len(a)):
    
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            s1+=a[j]
        else:
            s2+=a[j]
  
    
    r=s1*s2
    s1=s2=0
    l.append(r)
print(l)

