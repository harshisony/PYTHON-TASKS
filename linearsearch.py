print("enter elements:")
a=list(map(int,input().split()))
s=int(input())
for i in range(len(a)):
    if(a[i]==s):
        print(s," found at ",i+1)
        break
if(i==len(a)-1):
    print("not found")