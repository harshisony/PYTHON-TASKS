n = int(input())
s=str(n)
original = n  # Save original number before modification

# Using string manipulation to reverse the number
reverse_string = s[::-1]
print("Reversed Number (string method):", reverse_string)

# Using integer arithmetic to reverse the number
reverse = 0
while n != 0:
    rem = n % 10
    reverse = reverse * 10 + rem
    n //= 10  # Use integer division to discard the remainder
print("Reversed Number (integer arithmetic method):", reverse)

# Checking if both methods produce the same result
if reverse_string== str(reverse):
    print("Both methods produced the same reversed number.")
else:
    print("The reversed numbers from both methods are different.")
