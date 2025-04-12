import heapq
from typing import List, Tuple
from disjoint_set import DisjointSet

def kruskal_algorithm(graph: dict) -> Tuple[List[List[str]], int]:
    # add all the possible edges from the graph to weighted edge list
    weighted_edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, vertex, weight) not in weighted_edges:
                weighted_edges.append((weight, vertex, neighbors))

    # sort the edges based on weight i.e. key.first
    weighted_edges.sort()
    
    # find all the vertices and initialize DisjointSet class
    vertices = list(graph.keys())
    disjoint_set = DisjointSet(vertices)
    
    # finding the mst
    mst_edges = []
    total_cost = 0
    for weight, prev_node, next_node in weighted_edges:
        root_prev_node = disjoint_set.find(prev_node)
        root_next_node = disjoint_set.find(next_node)
        
        if root_prev_node != root_next_node:
            mst_edges.append((prev_node, next_node))
            total_cost += weight
            disjoint_set.union(root_prev_node, root_next_node)
    
    return mst_edges, total_cost

# graph is a weighted graph. For each node we have all 
# its neighbors and weighted edge to that neighbor
# DIFFERENCE B/W KRUSKAL's and PRIMS in forming Minimum Spanning Tree (MST): 
# kruskal uses sorted-edges + disjoint-set (union-find method) where as prims uses minimum-priority-queue
def primsAlgorithm(graph: dict, start: str) -> Tuple[List[List[str]], int]:
    priority_queue = []
    visited = set()
    
    # adding neigbors of the start node to the priority queue
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(priority_queue, (weight, start, neighbor))
    
    # forming a mst
    mst_edges = []
    total_cost = 0
    while priority_queue:
        # pop edges from priority queue with min edge weight
        (weight, prev_node, next_node) = heapq.heappop(priority_queue)
        
        if next_node not in visited:
            visited.add(next_node)
            print((prev_node, next_node), total_cost + weight)
            mst_edges.append((prev_node, next_node))
            total_cost += weight
            
            # add edges connecting neighbors of next_node to next_node to the priority queue
            for neighbor, weight in graph[next_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, next_node, neighbor))
    
    return mst_edges, total_cost

if __name__ == "__main__":
    # weighted undirected graph with all connected nodes (i.e., contains one set of nodes only)
    graph = {
        "A":[("F", 3), ("B", 2), ("D", 5)],
        "B":[("A", 2), ("F", 4), ("D", 2), ("C", 7)],
        "C":[("B", 7), ("D", 1)],
        "D":[("A", 5), ("B", 2), ("C", 1)],
        "F":[("A", 3), ("B", 4)]
    }
    
    # prims takes a weighted undirected graph and a starting node
    (mst_edges, total_cost) = primsAlgorithm(graph, "A")
    print("PRIMS: mst:{}, cost:{}".format(mst_edges, total_cost))
    
    # kruskal takes only a weighted undirected graph
    (mst_edges, total_cost) = kruskal_algorithm(graph)
    print("KRUSKAL: mst:{}, cost:{}".format(mst_edges, total_cost))
