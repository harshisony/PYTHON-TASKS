#list comprehension =  a way to create a new list with less syntax
#can mimic certain lambda functions, easier to read
#list = [expression for item in iterable]
#list = [expression for item in iterable if conditional]
#list = [expression if/else for item in iterable]

#normal way
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

#list comprehension
#create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1,11)]
print(squares)

student=[100,80,60,40,30,0]
passed=[i for i in student if i>=60]
print(passed)
all_list=["PASS" if i>=60 else "Fail" for i in student]
print(all_list)