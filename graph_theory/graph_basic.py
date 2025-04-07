from typing import List

def buildUndirectedGraph(edges: List[List[int]]) -> dict:
    graph = {}
    for edge in edges:
        ptA, ptB = edge
        
        if ptA not in graph.keys() and ptA is not None:
            graph[ptA] = set()
        
        if ptB not in graph.keys() and ptB is not None:
            graph[ptB] = set()
        
        graph[ptA].add(ptB)
        if ptB is not None:
            graph[ptB].add(ptA)
    
    return graph

def buildDirectedGraph(edges: List[List[int]]) -> dict:
    graph = {}
    for edge in edges:
        ptA, ptB = edge
        
        if ptA not in graph.keys() and ptA is not None:
            graph[ptA] = set()
            
        if ptB not in graph.keys() and ptB is not None:
            graph[ptB] = set()
            
        graph[ptA].add(ptB)
    
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
    
    # graph can have unconnectec components: say just one node unconnected to any other nodes
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [40, 500], [50, 60],
        [17, None], [19, None]
    ]
    directed_graph = buildDirectedGraph(edges_directed)
    print(directed_graph) 