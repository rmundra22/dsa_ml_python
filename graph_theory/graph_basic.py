from typing import List

def buildUndirectedGraph(edges: List[List[int]]) -> dict:
    graph = {}
    for edge in edges:
        ptA, ptB = edge
        
        if ptA not in graph.keys():
            graph[ptA] = set()
        
        if ptB not in graph.keys():
            graph[ptB] = set()
            
        graph[ptA].add(ptB)
        graph[ptB].add(ptA)
    
    return graph
    
    
if __name__ == "__main__":
    # edges = [
    #     [1, 2], [3, 4], [4, 5], [2, 4], [5, 1]
    # ]
    
    total_edges = int(input("Enter count of edges you want: "))
    edges = []
    for i in range(total_edges):
        edges.append(input().split())
        
    graph = buildUndirectedGraph(edges)
    print(graph) # {1: [2, 5], 2: [1, 4], 3: [4], 4: [3, 5, 2], 5: [4, 1]}
    