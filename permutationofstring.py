from itertools import permutations
a=input()
l=[]
for i in permutations(a):
    p=''.join(i)
    l.append(p)
print(l)
print(len(l))
    

#words = [''.join(p) for p in permutations('prio')]

#print(words)