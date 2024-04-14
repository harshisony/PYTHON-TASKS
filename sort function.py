#sort() method   = used with lists
#sorted() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
#students.sort(key=age,reverse=True) #if students is a list   # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)  #sorts according to grade i.e 1st index
    

students=['A','C','B','V','L']
students.sort()
print(students) #O/P:['A', 'B', 'C', 'L', 'V']

s=['A','C','B','V','L']
s.sort(reverse=True)
print(s) #O/P:['V', 'L', 'C', 'B', 'A']

s=('A','C','B','V','L')
p=sorted(s) #as it is a tuple we should use sorted function
print(p) #O/P:['A', 'B', 'C', 'L', 'V']

s=('A','C','B','V','L')
p=sorted(s,reverse=True)
print(p) #O/P:['V', 'L', 'C', 'B', 'A']