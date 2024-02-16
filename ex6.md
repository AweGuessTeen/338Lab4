Exercise 6:

1.
Arrays excel in quick access to elements by index, making random access and searching efficient, but they have fixed sizes, leading to potential memory inefficiencies. 
Linked lists provide dynamic memory allocation, making insertions and deletions efficient, but they lack direct index access.
The choice depends on use case specifics: arrays for frequent random access, linked lists for dynamic data with many insertions and deletions.

2.
To minimize the impact of a replace function in arrays, locate the target for replacement, perform deletion, and insert the new element separately.
This approach ensures each task's time complexity is proportional to the affected elements, optimizing efficiency.

3.
For a doubly linked list with a sort function, both Insertion Sort and Merge Sort work. Insertion Sort iterates through the list,
placing each element in the correct spot. Merge Sort recursively divides and merges the list. Insertion Sort has O(n^2) complexity, while Merge Sort has O(n log n).
The linked list's efficient insertion and deletion differentiate their performance from applying these sorts to a regular array.