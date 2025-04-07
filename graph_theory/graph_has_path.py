from collections import deque
from graph_basic import buildDirectedGraph, buildUndirectedGraph

def directedGraphHasPathDFS(graph: dict, source: int, destination: int) -> bool:
    """ Directed Graph: Has path from source to destination or not using DFS

    Args:
        graph (dict): _description_
        source (int): _description_
        destination (int): _description_

    Returns:
        bool: _description_
    """
    stack = deque([source])
    visited = set([source])
   
    while stack:
        vertex = stack.pop()
        if vertex == destination:
            return True
        
        for v in graph[vertex]:
            if v == destination:
                return True
            
            if v not in visited:
                visited.add(v)
                stack.append(v)
            
    return False

def directedGraphHasPathBFS(graph: dict, source: int, destination: int) -> bool:
    """ Directed Graph: Has path from source to destination or not using BFS

    Args:
        graph (dict): _description_
        source (int): _description_
        destination (int): _description_

    Returns:
        bool: _description_
    """
    queue = deque([source])
    visited = set([source])
   
    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            return True
        
        for v in graph[vertex]:
            if v == destination:
                return True
            
            if v not in visited:
                visited.add(v)
                queue.append(v)
            
    return False

def countConnectedComponents(graph: dict) -> int:
    total_components = 0
    stack = deque()
    visited = set()
    
    for k in graph.keys():
        if k not in visited:
            stack.append(k)
            visited.add(k)
            while stack:
                vertex = stack.pop()
                
                for neighbour in graph[vertex]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)
            total_components += 1
            print(k, total_components)
    
    return total_components

if __name__ == "__main__":
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [40, 500], [50, 60]
    ]
    directed_graph = buildDirectedGraph(edges_directed)
    print(directed_graph)
    print(directedGraphHasPathDFS(directed_graph, 100, 500))
    
    # revert edge from 500 -> 40 instead of 40 -> 500
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [500, 40], [50, 60], 
        [17, None], [19, None]
    ]
    directed_graph = buildDirectedGraph(edges_directed)
    print(directed_graph)
    print(directedGraphHasPathDFS(directed_graph, 100, 500))
    print(directedGraphHasPathDFS(directed_graph, 100, 100))
    print(directedGraphHasPathDFS(directed_graph, 100, 60))
    print(directedGraphHasPathDFS(directed_graph, 60, 100))
    
    print(directedGraphHasPathBFS(directed_graph, 100, 500))
    print(directedGraphHasPathBFS(directed_graph, 100, 100))
    print(directedGraphHasPathBFS(directed_graph, 100, 60))
    print(directedGraphHasPathBFS(directed_graph, 60, 100))
    
    # undirected graph with below mentioned nodes will show 2 components
    # directed graph with below nodes will show 3 components
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [500, 40], [50, 60], 
        [17, None], [19, 99]
    ]
    
    directed_graph = buildUndirectedGraph(edges_directed)
    total_components = countConnectedComponents(directed_graph)
    print(total_components)
    