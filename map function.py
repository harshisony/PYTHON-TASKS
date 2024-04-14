
#map() =   applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable) The function to apply to each item of the iterable. This can be a built-in function, 
# a user-defined function, or a lambda function.

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
    
    
    
# Define a function to square a number
def square(x):
    return x ** 2

# Apply the square function to each item of the iterable
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the result to a list
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]



# Using map with a lambda function to double each number in the list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)

# Convert the result to a list
doubled_numbers_list = list(doubled_numbers)
print(doubled_numbers_list)  # Output: [2, 4, 6, 8, 10]
