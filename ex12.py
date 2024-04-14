a=list(map(int,input().split()))
l=[]
for i in a:
    if i>9:
        n=i
        s=0
        while (n!=0):
            s+=(n%10)
            n=n//10
        l.append(s)
    else:
        l.append(i)
f=sum(l)
f1=f%10
k=sum(a)
f2=k%10

print(f1-f2)