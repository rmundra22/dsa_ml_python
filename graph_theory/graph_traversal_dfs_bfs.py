from collections import deque

# "TRICK: it is no (B)ull-(S)hit i.e. BFS is not stack but Queue and so DFS is stack"
class graph:
    
    def __init__(self, gdict = None):
        self.gdict = gdict if gdict else {}
    

def dfsRecursion(graph, start, visited):
    """Check for the visited and unvisited nodes
    BFS with recursion doesn't make sense but it is doable
    """        
    if start in visited:
        return
    
    print(start)
    visited.add(start)
    for neighbor in graph[start]:
        # pass by reference (visited) is required for this to work
        dfsRecursion(graph, neighbor, visited)


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


def dfs_flood_fill_or_island_count(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    
    # all kinds of boundary conditions or if the cell is visited => pass
    if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1'):
        return
    
    grid[r][c] = '0'  # mark as visited
    dfs_flood_fill_or_island_count(grid, r + 1, c)
    dfs_flood_fill_or_island_count(grid, r - 1, c)
    dfs_flood_fill_or_island_count(grid, r, c + 1)
    dfs_flood_fill_or_island_count(grid, r, c - 1)



if __name__ == "__main__":
    gdict = { 
        "a" : set(["b","c", "e"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e", "b", "c"]),
        "e" : set(["a", "d"])
    }
    visited = set()
    dfsRecursion(gdict, 'a', visited)
    print(dfsUsingStack(gdict, 'a')) # ['a', 'b', 'd', 'e', 'c']
    print(bfsUsingQueue(gdict, "a")) # ['a', 'c', 'b', 'd', 'e']