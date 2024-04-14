# Define some functions
def greet():
    return "Hello!"

def farewell():
    return "Goodbye!"

# Assign functions to variables
my_greeting = greet #this will assign greet memory location to my_greeting so we can use my_greeting as a function
my_parting = farewell
say=print

# Call the functions using the variables
print(my_greeting())  # Output: Hello!
print(my_parting())   # Output: Goodbye!
say("Harshiiii")