a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
s=0
a2.reverse()
for i in range(len(a1)):
    
        s+=a1[i]*a2[i]
print(s)
        
        
