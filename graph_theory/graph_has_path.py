from collections import deque
from graph_theory.graph_basic import buildDirectedGraph

# Directed Graph: Has path from source to destination or not
def graphHasPath(graph: dict, source: int, destination: int) -> bool:
    stack = deque(source)
    visited = set(source)
    
    while stack:
        vertex = stack.pop()
        
        for v in graph[vertex]:
            if v == destination:
                return True
            
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
    
    print(graphHasPath(directed_graph, 100, 500))