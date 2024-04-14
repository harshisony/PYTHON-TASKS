#max in 1st array,min in 2nd array
#max(1,2)
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
l1=[]
l2=[]
k=int(input())
for i in a1:
    if (i>9):
        l1.append(i)
for i in a2:
    if(i<9):
        l2.append(i)
print(max(len(l1),len(l2)))