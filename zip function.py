#zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#creates a zip object with paired elements stored in tuples for each element
# Define two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

# Use zip to combine the two lists into tuples
zipped_data = zip(names, ages)
print(zipped_data)
# Convert the result to a list (or iterate over it directly)
zipped_data_list = list(zipped_data)
print(zipped_data_list)  # Output: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

d=dict(zip(names,ages))
print(d)