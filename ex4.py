def latest(n,n1,n2):
    if(n%n1==0 and n%n2==0):
        return True
    else:
        return false
n=int(input())
n1=int(input())
n2=int(input())
res=latest(n,n1,n2)
print(res)
