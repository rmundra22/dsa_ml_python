Algorithms are unambiguous steps which should give us a well-defined output by processing zero or more inputs. This leads to many approaches in designing and writing the algorithms. It has been observed that most of the algorithms can be classified into the following categories.


# Greedy Algorithms
Greedy algorithms try to find a localized optimum solution, which may eventually lead to globally optimized solutions. However, generally greedy algorithms do not provide globally optimized solutions.

So greedy algorithms look for a easy solution at that point in time without considering how it impacts the future steps. It is similar to how humans solve problems without going through the complete details of the inputs provided.

Most networking algorithms use the greedy approach. Here is a list of few of them −

* Travelling Salesman Problem
* Prim's Minimal Spanning Tree Algorithm
* Kruskal's Minimal Spanning Tree Algorithm
* Dijkstra's Minimal Spanning Tree Algorithm


# Divide and Conquer
This class of algorithms involve dividing the given problem into smaller sub-problems and then solving each of the sub-problem independently. When the problem can not be further sub divided, we start merging the solution to each of the sub-problem to arrive at the solution for the bigger problem.

The important examples of divide and conquer algorithms are −

* Merge Sort
* Quick Sort
* Kruskal's Minimal Spanning Tree Algorithm
* Binary Search


# Dynamic Programming
Dynamic programming involves dividing the bigger problem into smaller ones but unlike divide and conquer it does not involve solving each sub-problem independently. Rather the results of smaller sub-problems are remembered and used for similar or overlapping sub-problems.

Mostly, these algorithms are used for optimization. Before solving the in-hand sub-problem, dynamic algorithm will try to examine the results of the previously solved sub-problems.Dynamic algorithms are motivated for an overall optimization of the problem and not the local optimization.

The important examples of Dynamic programming algorithms are −

* Fibonacci number series
* Knapsack problem
* Tower of Hanoi


## Content

> Data Structure
```
 1. Binary Tree: create (insert), remove, print (in-order, pre-order, post-order), traversal, search
 2. Graphs (TODO)
 3. Hash Tables (TODO)
 4. Heaps and Maps (TODO, using with and without heapify library)
 5. Linked List: insert, insert_at, replace, print, length, remove_at 
 6. Doubly Linked List: add elements, insert, print
 7. Stacks and Queues (TODO)
 8. Trie: search, insert
 9. Arrays and string
```

> Algorithms (Add comments for time and space complexity)
```
 1. Searching Algorithms: Linear, Binary
 2. Sorting Algorithms: Bubble, Quick, Insertion, Shell (TODO), Selection, Heap (TODO), Merge, Radix (TODO), Bucket (TODO), Counting (TODO)
 3. Greedy Algorithms: Dijkstra's Algorithm (using with and without Heapipy library)
 4. Graph Algorithms: BFS, DFS (using collections library)
 5. Bit Manipulation
 6. Dynamic Programming (TODO)
 7. Backtracking (TODO)
 8. Hashing (TODO)
```

> ML (ML Case Studies and Design)
```
 1. K Means Clustering
 2. Movie Recommendor for Flights
 3. Tensorflow 2 for experts
 4. Python Basics (TODO)
 5. Pyspark Basics (TODO)
```

> Probability Problems in action
```
 1. Bayes Theorem Problems (TODO)
 2. Markov Chains
```

## References
```
 1. Binary Tree: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
```