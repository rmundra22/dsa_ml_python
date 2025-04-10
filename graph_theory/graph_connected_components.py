from collections import deque
from graph_basic import buildDirectedGraph, buildUndirectedGraph

def countConnectedComponents(graph: dict) -> int:
    total_components = 0
    stack = deque()
    visited = set()
    
    connected_components = []
    for k in graph.keys():
        if k not in visited:
            stack.append(k)
            visited.add(k)
            nodes_in_components = 1
            new_component = set([k])
            while stack:
                vertex = stack.pop()
                
                if vertex in graph.keys():
                    for neighbour in graph[vertex]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            stack.append(neighbour)
                            
                            if neighbour:
                                nodes_in_components += 1
                                new_component.add(neighbour)
                else:
                    break
                
            connected_components.append(new_component)
            total_components += 1
            print(k, total_components, nodes_in_components, connected_components)
    
    return total_components

def bfsShortestRoad():
    queries = int(input())
    result = {}
    for q in range(queries):
        graph = {}
        start_node = -1
        nodes, edges = map(int, input().split())
        
        connections = []
        for node in range(1, nodes+1):
            connections.append([node, None])
        
        for _ in range(edges):
            start, end = map(int, input().split())
            connections.append([start, end])
        
        # one can use graph with adjacency list to avoid handling of nodes with no connections etc. 
        graph = buildUndirectedGraph(connections)    
        start_node = int(input())
    
        queue = deque([start_node])
        visited = []
        distance = [-1] * nodes
        level = 1
        print(start_node, graph)
        
        while queue:
            vertex = queue.popleft()
            visited.append(vertex)
            
            for neighbour in graph[vertex]:
                if neighbour not in visited and neighbour is not None:
                    distance[neighbour-1] = 6 * level
                    visited.append(neighbour)
                    queue.append(neighbour)
                    print(neighbour, distance)
            
            level += 1

        print(distance)
        result[q] = distance[:start_node-1] + distance[start_node:]
        print(result[q])
        
    return result
        
    
        
    

if __name__ == "__main__":
    # undirected graph with below mentioned nodes will show 2 components
    # directed graph with below nodes will show 3 components
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [500, 40], [50, 60], 
        [17, None], [19, 99], [99, 101]
    ]
    
    directed_graph = buildUndirectedGraph(edges_directed)
    total_components = countConnectedComponents(directed_graph)
    print(total_components)
    
    bfsShortestRoad()
    