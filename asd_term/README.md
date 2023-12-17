Task
Implement an algorithm for finding a minimum spanning tree based on Kruskal's algorithm.

Input Data
Any text file containing the adjacency matrix of the graph in the following format:

```
A B C
0 3 1
3 0 2
1 2 0
```

Where the first line consists of a space-separated list of all edges, followed by the adjacency matrix. In the matrix, a value of 0 indicates no edge between the vertices, and a positive number corresponds to the weight when an edge between the vertices exists.

The output should consist of pairs sorted by name and the total weight:

```
A C
B C
3
```

Maximum input size: 50 vertices. Vertices can be specified by any text sequence without spaces. The edge weight is limited to the range from 1 to 1023, inclusive.