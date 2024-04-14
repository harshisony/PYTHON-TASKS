import time

# Get the current time
current_time = time.time()
print("Current time:", current_time)

# Convert current time to a string
formatted_time = time.ctime(current_time)
print("Formatted time:", formatted_time)

# Sleep for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")

# Convert current time to time tuple
time_tuple = time.localtime(current_time)
print("Time tuple:", time_tuple)

# Format time tuple as a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print("Formatted time:", formatted_time)
