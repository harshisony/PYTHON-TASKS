def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input())
res=fact(num)
print("fact of ",num," is",res)
