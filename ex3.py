# ex3.py

import sys
import timeit
import matplotlib.pyplot as plt

# 1. The strategy for growing Python lists involves allocating a new, larger array and copying
# the elements from the old array to the new one when the current array is full. The growth factor
# is implementation-dependent, but typically the list size is increased by a certain ratio,
# often around 1.125 times the current size for CPython.

# 2. Test code to observe list capacity changes
def observe_capacity_changes():
    capacities = []
    for i in range(64):
        lst = [0] * i
        capacity = sys.getsizeof(lst)
        if not capacities or capacity != capacities[-1]:
            capacities.append((i, capacity))
            print(f"Capacity changed at size {i}: {capacity} bytes")
    return capacities[-1][0] 


def measure_growth_time(initial_size, append_times=1, repeat=1000):
    statement = f"lst = [0] * {initial_size}\n" + "lst.append(None)" * append_times
    setup = "lst = []"
    return timeit.repeat(stmt=statement, setup=setup, number=1, repeat=repeat)


S = observe_capacity_changes()

# 3. Measure time for array growth from S to S+1
times_S_to_S_plus_1 = measure_growth_time(S)

# 4. Measure time for array growth from S-1 to S
times_S_minus_1_to_S = measure_growth_time(S-1)

# 5. Plotting the distribution of measurements
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(times_S_to_S_plus_1, bins=30, color='blue', alpha=0.7)
plt.title('Time Distribution for S to S+1')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(times_S_minus_1_to_S, bins=30, color='red', alpha=0.7)
plt.title('Time Distribution for S-1 to S')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Discussion: The histograms show the distribution of times it takes to append an element to a list
# at critical sizes. This can help in understanding the efficiency of Python's list operations
# and the impact of memory reallocation on performance.