#multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#multiprocessing = better for cpu bound tasks (heavy cpu usage)
#multithreading = better for io bound tasks (waiting around)
import multiprocessing
import time

def square(x):
    return x * x

if __name__ == "__main__":
    # Create a pool of processes
    pool = multiprocessing.Pool()

    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Apply the square function to each number using multiple processes
    results = pool.map(square, numbers)

    # Close the pool to free up resources
    pool.close()

    # Wait for all processes to finish
    pool.join()

    print("Results:", results)
