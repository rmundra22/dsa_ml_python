import heapq
from typing import List, Tuple

# graph is a weighted graph. For each node we have all 
# its neighbors and weighted edge to that neighbor
# DIFFERENCE B/W KRUSKAL's and PRIMS in forming Minimum Spanning Tree (MST): 
# kruskal used Union-Find method where as prims uses priority queue
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
    (mst_edges, total_cost) = primsAlgorithm(graph, "A")
    print(mst_edges, total_cost)
