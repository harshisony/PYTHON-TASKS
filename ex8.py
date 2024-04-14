a=list(map(int,input().split()))
a.reverse()
s=0

for i in range(len(a)):
    l=[]
    if (i==0):
        s+=a[i]
    else:
        for j in range(0,i+1):
            if(a[i]>a[j]):
                l.append(a[j])
        if (len(l)==i):
            s+=a[i]
            del(l)
            
        
        
print(s)                

                
            
        