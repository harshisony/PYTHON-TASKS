print("enter elements:")
a=list(map(int,input().split()))
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("sorted:",*a)
print("sorted:",a)
a=','.join(str(i) for i in a)
print("sorted:",a)

#a=','.join(map(str, a))
#print("sorted:",*a) o/p:1,2,3

