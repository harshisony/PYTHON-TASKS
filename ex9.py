s=input()
if (len(s)==0):
    print(0)
else:
    l=[]
    res=1
    l.append(res)
    for i in range(2,27):
        res=res*10
        l.append(res)
    d={}
    j=0
    for i in range(ord('A'),ord('Z')+1):
        d[chr(i)]=l[j]
        j+=1
    m=list(s)
    f=[]
    for i in m:
        f.append(d[i])
    print(sum(f))
        