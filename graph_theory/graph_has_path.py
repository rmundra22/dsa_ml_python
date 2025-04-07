from collections import deque
from graph_basic import buildDirectedGraph

def directedGraphHasPath(graph: dict, source: int, destination: int) -> bool:
    """ Directed Graph: Has path from source to destination or not

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


if __name__ == "__main__":
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [40, 500], [50, 60]
    ]
    directed_graph = buildDirectedGraph(edges_directed)
    print(directed_graph)
    print(directedGraphHasPath(directed_graph, 100, 500))
    
    # revert edge from 500 -> 40 instead of 40 -> 500
    edges_directed = [
        [100, 10], [10, 20], [20, 30], 
        [30, 70], [30, 40], [30, 60],
        [40, 50], [500, 40], [50, 60]
    ]
    directed_graph = buildDirectedGraph(edges_directed)
    print(directed_graph)
    print(directedGraphHasPath(directed_graph, 100, 500))
    print(directedGraphHasPath(directed_graph, 100, 100))
    print(directedGraphHasPath(directed_graph, 100, 60))
    print(directedGraphHasPath(directed_graph, 60, 100))
    