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
    