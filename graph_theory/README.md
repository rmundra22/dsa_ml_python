# Graph Theory

> Reference: https://www.youtube.com/watch?v=seDbFvnidnw&list=PLPdtS77PaSuvssIsG1-39AC_31BLu2UUf&index=1&pp=iAQB


✅ 1. Graph Representations
* Adjacency List vs Adjacency Matrix
* Directed vs Undirected graphs
* Weighted vs Unweighted graphs
> Graph input parsing (edge list, matrix, etc.)

✅ 2. Graph Traversals
* Depth-First Search (DFS) - Recursive & iterative
* Breadth-First Search (BFS) - Queue-based and Level order traversal (esp. in trees)
> Use cases: connectivity, pathfinding, cycles, etc.

✅ 3. Cycle Detection
* In undirected graphs using DFS + parent tracking
* In directed graphs using visited + recursion stack (white-gray-black sets)
> Use cases: dependency resolution, deadlock detection

✅ 4. Topological Sorting (Directed Acyclic Graphs - DAGs)
* Kahn’s Algorithm (BFS-based)
* DFS-based topo sort
> Use cases: task scheduling, compiler ordering

✅ 5. Connected Components
* Counting components (DFS/BFS/Union-Find)
* Strongly Connected Components (Kosaraju’s or Tarjan’s Algorithm)
> Use cases: clustering, social networks

✅ 6. Shortest Path Algorithms
* Dijkstra's Algorithm (for weighted graphs, no negative weights)
* Bellman-Ford (handles negative weights)
* Floyd-Warshall (all-pairs shortest path)
* BFS (for unweighted graphs)
* A* (for pathfinding with heuristics)

✅ 7. Minimum Spanning Tree
* Prim's Algorithm
* Kruskal's Algorithm (requires Union-Find)
> Use cases: network design, clustering

✅ 8. Union-Find (Disjoint Set Union - DSU)
* With path compression + union by rank
> Use cases: cycle detection, Kruskal’s, connected components

✅ 9. Backtracking in Graphs
* Hamiltonian Path/Cycle
* All paths between nodes
* Word Ladder-type problems
* Maze/path-finding problems

✅ 10. Advanced Patterns (optional but useful)
* Tarjan's Bridge & Articulation Points
* Eulerian Path/Cycle
* Graph Coloring
* Bipartite Check (using BFS/DFS or 2-coloring)
* 0-1 BFS (Deque for edges with 0 or 1 weights)
* Top-K paths / Dijkstra variants

