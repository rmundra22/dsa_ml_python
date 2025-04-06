import collections


class graph:
    
    def __init__(self, gdict = None):
        self.gdict = gdict if gdict else {}
    
        
def dfs(graph, start, visited = None):
    """Check for the visited and unvisited nodes
    RE_CHECK: return is not stable
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    
    # graph elements are set so you can subtract the set(visited) from it
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def bfs(graph, startnode):
    """Track the visited and unvisited nodes using queue"""
    visited, queue = set([startnode]), collections.deque([startnode])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in visited:
                visited.add(node)
                queue.append(node)

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
    print(dfs(gdict, 'a'))
    # print(bfs(gdict, "a"))