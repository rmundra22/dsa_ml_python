from typing import List
from collections import deque, defaultdict

# leet code problem: #269
# ✅ Used defaultdict(set) for clean graph updates.
# ✅ Avoided index errors by using for j in range(min_len) and checking mismatch.
# ✅ Used Kahn’s algorithm (topological sort with BFS) which is more intuitive and easier to debug than recursive DFS in this context.
# ✅ Clean cycle detection by comparing length of result to in_degree.
def alienDictionaryKahnAlgorithm(words: List[str]) -> str:
    # Step 1: Create graph
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        
        # Edge case: Prefix issue
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""
        
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break  # Only the first difference matters

    # Step 2: Topological Sort (BFS using Kahn's algorithm)
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Check for cycle
    if len(result) < len(in_degree):
        return ""

    return ''.join(result)

# TODO: Correct the code : not working as expecetd
def alienDictionary(words: List[str]) -> str:
    # create a graph    
    graph = { c:set() for w in words for c in w }

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        
        # edge case: need to return for no solution
        if w1[:min_len] == w2[:min_len] and len(w1) > min_len:
            return ""
        
        i = 0
        while w1[i] == w2[i]:
            i += 1
        
        graph[w1[i]].add(w2[i])
    
    print(graph)
    # traverse a graph using dfs (post order traversal)
    start = w1[0]
    stack = deque([start])
    
    # if a node is not in visited as key than that node was not visited
    # TRUE: visited but in current path
    # FALSE: visited and a leaf node
    visited = {start: True}
    
    ans = []
    while stack:
        vertex = stack.pop()
        
        for neighbour in graph[vertex]:
            
            if neighbour not in visited.keys():
                stack.append(neighbour)
                visited[neighbour] = True
            else:
                visited[neighbour] = False
                ans.append(neighbour)
            
            visited[neighbour] = False
                
    # reverse the solution to get topologically sorted answer
    n = len(ans)
    answer = []
    for i in range(n-1, -1, -1):
        if len(answer) == 0:
            answer = [ans[i]]
        else:
            answer.append(ans[i])
            
    return answer
    
if __name__ == "__main__":
    # ANSWERS: ["wertf", "", ""]
    word_list = [
        ["wrt", "wrf", "er", "ett", "ftt"],
        ["wrt", "wrf", "apes", "ape", "ftt"],
        ["wrt", "ett", "wrt"],
    ]
    
    for words in word_list:
        topo_sort = alienDictionaryKahnAlgorithm(words)
        print(words, topo_sort)
            