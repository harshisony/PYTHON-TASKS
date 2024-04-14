a=input()
l=list(a)
d={}
for i in l:
    d[i]=d.get(i,0)+1
for i in d:
    b='$'*d[i]
    print(i,":",b,end=",")
