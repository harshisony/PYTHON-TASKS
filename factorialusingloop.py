n=int(input())
fact=1
if n<0:
    print("negative")
elif n==0:
    print("fact of ",n,"is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of ",n,"is ",fact)