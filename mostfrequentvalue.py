def most_frequent_value(lst):
    # Create an empty dictionary to store element counts
    counts = {}
    
    # Iterate through the list and count occurrences of each element
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    # Find the element with the highest count (most frequent)
    most_frequent = max(counts, key=counts.get)
    frequency = counts[most_frequent]
    
    return most_frequent, frequency

test_list = [1, 2, 3, 9, 2, 7, 3, 5, 9, 9, 9]
most_frequent, frequency = most_frequent_value(test_list)

print(f"The most frequent value is: {most_frequent}")
print(f"It appears {frequency} times in the list.")
