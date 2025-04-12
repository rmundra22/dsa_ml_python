from typing import List
from collections import deque, defaultdict

# leet code problem: #269
# ✅ Used defaultdict(set) for clean graph updates.
# ✅ Avoided index errors by using for j in range(min_len) and checking mismatch.
# ✅ Used Kahn’s algorithm (topological sort with BFS) which is more intuitive and easier to debug than recursive DFS in this context.
# ✅ Clean cycle detection by comparing length of result to in_degree.
def alienDictionaryBfsKahnAlgorithm(words: List[str]) -> str:
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

# This version uses recurive dfs
def alienDictionaryDfsIterative(words: List[str]) -> str:
    # Step 1: Build the graph
    graph = defaultdict(set)
    for word in words:
        for c in word:
            graph[c]  # ensures all characters are included

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        # Invalid case: prefix conflict
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break

    # Step 2: Iterative DFS with cycle detection
    visited = {}  # node -> 'unvisited', 'visiting', 'visited'
    result = []

    for node in graph:
        if node in visited:
            continue

        stack = [(node, False)]  # (node, is_post)
        path = set()  # nodes in current path for cycle detection

        while stack:
            current, is_post = stack.pop()

            if is_post:
                visited[current] = "visited"
                result.append(current)
                path.discard(current)
                continue

            if current in visited:
                if visited[current] == "visiting":
                    return ""  # cycle detected
                continue

            visited[current] = "visiting"
            path.add(current)

            stack.append((current, True))  # Post-order marker

            for neighbor in graph[current]:
                if neighbor in path:
                    return ""  # cycle detected
                if neighbor not in visited:
                    stack.append((neighbor, False))

    result.reverse()
    return ''.join(result)
    
if __name__ == "__main__":
    # ANSWERS: ["wertf", "", ""]
    word_list = [
        ["wrt", "wrf", "er", "ett", "ftt"],
        ["wrt", "wrf", "apes", "ape", "ftt"],
        ["wrt", "ett", "wrt"],
    ]
    
    for words in word_list:
        topo_sort = alienDictionaryBfsKahnAlgorithm(words)
        print(words, topo_sort)
        
    for words in word_list:
        topo_sort = alienDictionaryDfsIterative(words)
        print(words, topo_sort)
            