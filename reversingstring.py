def reverse_string(input_string):
    return input_string[::-1]

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "!dlroW ,olleH"

#using reversed function

def reverse_string(input_string):
    return ''.join(reversed(input_string))

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "!dlroW ,olleH"

#using loop

def reverse_string(input_string):
    reversed_str = ''
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string)  # Output: "!dlroW ,olleH"
