# Min-Heap
# A min-heap is a complete binary tree where the value of each node is less than or equal to the values of its children.
# The smallest element in the heap is at the root.
# Each node's value is less than or equal to the values of its children.

# Basic Operations:

# 1. Insertion:
# To insert an element into a min-heap, add it to the end of the heap (as the leftmost available position in the last level).
# Then, compare the inserted element with its parent. If the parent's value is greater, swap the elements.
# Repeat this process until the element is in its correct position or becomes the root.

# 2. Deletion (Extract Min):
# To remove the minimum element (root) from a min-heap, replace the root with the last element in the heap.
# Then, compare the new root with its children. Swap it with the smaller child if necessary.
# Continue this process until the element is in its correct position or becomes a leaf node.

# 3. Heapify:
# Heapify is the process of creating a heap from an array of elements. It rearranges the elements in the array
# so that the resulting binary tree satisfies the heap property.

# Time Complexity:
# - Insertion: O(log N) where N is the number of elements in the heap.
# - Deletion: O(log N)
# - Heapify: O(N) where N is the number of elements in the array.

# Applications:
# - Priority queues
# - Heap sort algorithm
# - Implementations of algorithms like Dijkstra's shortest path algorithm

# Variants:
# - Max-Heap: Similar to a min-heap, but the largest element is at the root.
# - Binomial Heap
# - Fibonacci Heap
