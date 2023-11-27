# Algorithms-and-Data-Structures-is-for-second-year-students
This repository contains practical assignments for the "Algorithms and Data Structures" course at ETU LETI, St. Petersburg University. It is designed for second-year students majoring in Information Systems and Technologies at the Department of Information Systems.


TASKS:
1)
Implement the following data structures: doubly linked list, dynamic array, and stack. The stack can be implemented based on either a list or separately. Use the stack to implement the Shunting Yard algorithm. Allowed symbols in the original expression: +, -, *, /, ^, sin, cos, (, ), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. To simplify tokenizing the input string, it is allowed to separate each symbol with a space.

2)
Implement Timsort. The implementation should include all the main elements of the algorithm: insertion sort, finding run sequences, calculating minrun, merging run sequences, and galloping mode during merging.

3)
Implement:
A regular binary tree (non-searching and non-balancing) with an implementation of depth-first traversal (the traversal direction is not important, recursive traversal is acceptable).
An algorithm for parsing bracket notation of the tree. Example: (8 (9 (5)) (1)) — root 8, left child 9, right child 1, left child of node 9 — 5.
AVL tree (advanced version — K-d tree) with implementation of insertion, deletion, search, breadth-first traversal, and depth-first traversal (all 3 types using the iterative approach).
Demonstrate:

Reading bracket notation (by reading from a file).
Step 1 either creates a binary tree or reports an error (incorrect symbols, incorrectly placed brackets, not a binary tree at all, etc.).
Traverse the obtained tree and create an AVL (or K-d) tree.
Demonstrate the output of all nodes in 4 ways: breadth-first and 3 depth-first traversals.
