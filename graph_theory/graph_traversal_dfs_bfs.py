from collections import deque


class graph:
    
    def __init__(self, gdict = None):
        self.gdict = gdict if gdict else {}
    
        
def dfsRecursion(graph, start, visited = None):
    """Check for the visited and unvisited nodes
    RE_CHECK: return is not stable
    """
    if visited is None:
        visited = set()
        
    visited.add(start)
    print(start)
    
    # graph elements are set so you can subtract the set(visited) from it
    for next in graph[start] - visited:
        dfsRecursion(graph, next, visited)



def bfs(graph, startnode):
    """Track the visited and unvisited nodes using queue"""
    visited = set([startnode]) 
    queue = deque([startnode])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
               
                
def dfsUsingStack(graph: dict, start_node: str) -> None:
    """ returns how the graph is traversed using dfs (stack based)"""
    visited = set([start_node])
    stack = deque([start_node])
    path = []
    while stack:
        temp = stack.pop()
        path.append(temp)
        
        for node in graph[temp]:
            if node not in visited:
                stack.append(node)
                visited.add(node)    
    return path

def flood_fill_algo():
    pass


if __name__ == "__main__":
    gdict = { 
        "a" : set(["b","c"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e"]),
        "e" : set(["a"])
    }
    dfsRecursion(gdict, 'a')
    # print(dfsUsingStack(gdict, 'a')) # ['a', 'b', 'd', 'e', 'c']
    # print(bfs(gdict, "a"))