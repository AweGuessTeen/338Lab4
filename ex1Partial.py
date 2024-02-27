import random
import array
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def binary_search(self, value):
        return self._binary_search(self.head, value)

    def _binary_search(self, head, value):
        start = head
        last = None

        while True:
            mid = self._get_middle(start, last)

            if mid is None:
                return None

            if mid.data == value:
                return mid

            elif mid.data < value:
                start = mid.next
            else:
                last = mid

            if not (last is None or last != start):
                break

        return None

    def _get_middle(self, start, last):
        if start is None:
            return None

        slow = start
        fast = start.next

        while fast != last:
            fast = fast.next
            if fast != last:
                slow = slow.next
                fast = fast.next

        return slow
    

class ArrayBinarySearch:
    def __init__(self):
        self.arr = array.array('i')

    def append(self, value):
        self.arr.append(value)

    def binary_search(self, value):
        return self._binary_search(0, len(self.arr) - 1, value)
    
    def _binary_search(self, left, right, value):
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1


def measure_performance(data_structure, size):
    data = None
    if data_structure == 'LinkedList':
        data = LinkedList()
    elif data_structure == 'ArrayBinarySearch':
        data = ArrayBinarySearch()

    for i in range(size):
        data.append(i)

    start_time = time.time()
    for _ in range(100):
        value = random.randint(0, size - 1)
        data.binary_search(value)
    end_time = time.time()

    return (end_time - start_time) / 100


# Test different input sizes
input_sizes = [1000, 2000, 4000, 8000]

# Initialize lists to store average times
avg_times_linked_list = []
avg_times_array = []

# Measure performance and store average times
for size in input_sizes:
    avg_time_linked_list = measure_performance('LinkedList', size)
    avg_times_linked_list.append(avg_time_linked_list)
    
    avg_time_array = measure_performance('ArrayBinarySearch', size)
    avg_times_array.append(avg_time_array)

# Plotting
plt.figure(figsize=(10, 6))

# Plot linked list performance
plt.plot(input_sizes, avg_times_linked_list, marker='o', label='Linked List', color='blue')

# Plot array performance
plt.plot(input_sizes, avg_times_array, marker='o', label='Array', color='green')

# Interpolation
x_new = np.linspace(min(input_sizes), max(input_sizes), 300)
f_linked_list = interp1d(input_sizes, avg_times_linked_list, kind='cubic')
f_array = interp1d(input_sizes, avg_times_array, kind='cubic')
plt.plot(x_new, f_linked_list(x_new), '--', label='Linked List (Interpolated)', color='navy')
plt.plot(x_new, f_array(x_new), '--', label='Array (Interpolated)', color='lime')

plt.title('Performance of Binary Search (Average Time)')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.xscale('log')  
plt.yscale('log')  
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


#Question 4
#The time complexity for a binary search of a linked list is O(n). 
#n represents the total number of nodes in the linked list, and since
#the binary search has to go through each node to find the value its 
#looking for, the complexity is O(n)