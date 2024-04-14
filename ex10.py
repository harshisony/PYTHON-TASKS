def p(k,n,a):
    count=0
    l=[]
    a.sort()
    i=1
    while(len(l)<k):
            
            for j in range(len(a)):
                if (i%a[j]==0):
                    break
            else: 
                l.append(i)
            i+=1
            
    return sum(l)
    
        
                     
k=int(input())
n=int(input())
a=list(map(int,input("Arr :").split()))
res=p(k,n,a)
print(res)