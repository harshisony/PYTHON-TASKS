'''Higher Order Function =  a function that either:
1. accepts a function as an argument
or
2. returns a function
(In python, functions are also treated as objects)'''

#accpets a function as an argument
def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Pass the 'add' function as an argument to 'apply_operation'
result1 = apply_operation(add, 5, 3)
print("Result of addition:", result1)  # Output: Result of addition: 8

# Pass the 'subtract' function as an argument to 'apply_operation'
result2 = apply_operation(subtract, 5, 3)
print("Result of subtraction:", result2)  # Output: Result of subtraction: 2


#returns a function
def divisor(x):
   def dividend(y):
       return y / x
   return dividend


divide = divisor(2)
print(divide(10))