n=int(input())
if n==1:
    print(n," is not prime")
elif n>1:

    flag=False
    for i in range(2,n):
        if(n%i==0):
            flag=True
            break
if flag:
    print(n," is not prime")
else:
    print(n, " is prime")