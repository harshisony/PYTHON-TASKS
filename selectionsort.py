print("enter elements:")
a=list(map(int,input().split()))
for i in range(len(a)-1):
    min=i
    for j in range(i+1,len(a)):
        if (a[min]>a[j]):
            min=j
    if(min!=i):
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
print("sorted:",*a)