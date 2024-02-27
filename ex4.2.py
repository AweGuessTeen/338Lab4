import time
import random
import matplotlib.pyplot as plt


#ineffecient implem.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#effecient implem
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def run_experiment():
    measurements_linear = []
    measurements_binary = []

    # Generate a large sorted array
    large_array = sorted(random.sample(range(1000000), 1000))

    for _ in range(100):
        # Random target within the array
        target = random.choice(large_array)

        # Measure time for linear search
        start_time = time.time()
        linear_search(large_array, target)
        end_time = time.time()
        measurements_linear.append(end_time - start_time)

        # Measure time for binary search
        start_time = time.time()
        binary_search(large_array, target)
        end_time = time.time()
        measurements_binary.append(end_time - start_time)

    return measurements_linear, measurements_binary

if __name__ == "__main__":
    measurements_linear, measurements_binary = run_experiment()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.hist(measurements_linear, bins=20, alpha=0.5, label='Linear Search')
    plt.hist(measurements_binary, bins=20, alpha=0.5, label='Binary Search')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Execution Time Distribution')
    plt.legend()
    plt.show()

#Worst-case Complexities
#For the linear search, the worst case complexity is O(n)
#For the binary search, the worst case complexity is O(log n)

