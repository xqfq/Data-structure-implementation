# Data structure implementation - Practice data structure implementation using python
## Directory
1. Stack
2. Queue
3. min-Heap

## Stack
### Description
An ordered data structure where the addition and the removal of items takes place at the top. Implements expandable stack via doubling the size the the existing stack
### Test
@Stack_test.py
### Application
1. Depth-first traversal
### Complexity analysis
Amortized analysis:\
T(n) = n + c + 2c + ... + n/c*c = n + c * (1 + 2 + ... + n/c) = n+ c * (1 + n/c) * n/c * 1/2 = O(n^2)\
T(n)/n = O(n)

## Queue
### Description
FIFO ordered data structure
### Test
@Queue_test.py
### Application
1. Breadth-first traversal
### Complexity analysis


## Min-Heap
### Description
Min-Heap is a tree-based data structure that satisfies the heap property, i.e. all nodes are less than or equal of its children
### Test
### Application
1. Priority queue
### Complexity analysis
