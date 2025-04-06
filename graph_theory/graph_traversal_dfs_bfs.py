from collections import deque


class graph:
    
    def __init__(self, gdict = None):
        self.gdict = gdict if gdict else {}
    

# wrong implementation
# def dfsRecursion(graph, start):
#     """Check for the visited and unvisited nodes
#     RE_CHECK: return is not stable
#     """        
#     print(start)
    
#     if len(graph[start]) == 0:
#         return
    
#     for val in graph[start]:
#        dfsRecursion(graph, val) 



def bfsUsingQueue(graph, startnode):
    """Track the visited and unvisited nodes using queue
    visted means that a node will be explored by adding all its adjacent nodes to visited
    Note - First visted will pop first hence we need FIFO => QUEUE Data Structue for bfs
    """
    visited = set([startnode]) 
    queue = deque([startnode])
    path = []
    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        
        for node in graph[vertex]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
    return path
               
                
def dfsUsingStack(graph: dict, start_node: str) -> None:
    """ returns how the graph is traversed using dfs (stack based)
    visted means that a node will be explored by adding all its adjacent nodes to visited
    Note - First visted will pop last hence we need LIFO => STACK Data Structue for dfs
    """
    visited = set([start_node])
    stack = deque([start_node])
    path = []
    while stack:
        vertex = stack.pop()
        path.append(vertex)
        
        for node in graph[vertex]:
            if node not in visited:
                stack.append(node)
                visited.add(node)    
    return path

def flood_fill_algo():
    pass


if __name__ == "__main__":
    gdict = { 
        "a" : set(["b","c", "e"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e", "b", "c"]),
        "e" : set(["a", "d"])
    }
    # dfsRecursion(gdict, 'a')
    print(dfsUsingStack(gdict, 'a')) # ['a', 'b', 'd', 'e', 'c']
    print(bfsUsingQueue(gdict, "a")) # ['a', 'c', 'b', 'd', 'e']