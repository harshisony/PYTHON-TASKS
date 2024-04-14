def count_vowels(string):
    # Initialize a dictionary to store the vowel counts
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    string = string.lower()

    # Loop through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in 'aeiou':
            # Increment the count for the corresponding vowel
            vowel_counts[char] += 1

    return vowel_counts

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = count_vowels(input_string)
    print("Number of each vowel:")
    for vowel, count in result.items():
        print(f"{vowel}: {count}")
