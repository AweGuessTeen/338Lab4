# Imports
import timeit
import matplotlib.pyplot as plt

# Node Class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def get_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def get_element_at_position(self, pos):
        current = self.head
        for _ in range(pos):
            current = current.next
        return current

    def old_reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size() - 1, -1, -1):
            currNode = self.get_element_at_position(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    def new_reverse(self):
        prevNode = None
        currNode = self.head
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode

# Main Code
sizes = [1000, 2000, 3000, 4000]
repetitions = 100

old_times = []
new_times = []

for size in sizes:
    setup_code = f"""
from __main__ import LinkedList, Node
linkedList = LinkedList()
for i in range({size}):
    node = Node(i)
    linkedList.insert_tail(node)
"""

    old_timer = timeit.Timer("linkedList.old_reverse()", setup=setup_code)
    old_total = old_timer.timeit(number=100)
    
    new_timer = timeit.Timer("linkedList.new_reverse()", setup=setup_code)
    new_total = new_timer.timeit(number=100)

    old_avg = old_total / repetitions
    new_avg = new_total / repetitions

    old_times.append(old_avg)
    new_times.append(new_avg)

# Plotting
plt.plot(sizes, old_times, label="Old")
plt.plot(sizes, new_times, label="New")
plt.xlabel("List Size")
plt.ylabel("Average Time (seconds)")
plt.title("Comparison of Reverse Methods")
plt.legend()
plt.show()