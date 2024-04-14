n=int(input())
a=0
b=1
c=0
if n<=0:
    print("invalid")
elif (n==1|n==2):
    print(a)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    print("fib:",c)