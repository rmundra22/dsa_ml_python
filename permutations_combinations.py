import string
from typing import List

def permutations(s: string) -> List:
    s = list(s)  # Convert string to list for easier swapping
    
    result = []
    n = len(s)
    
    def backtrack(start):
        if start == len(s):
            result.append("".join(s))
            return

        for i in range(start, n):
            # Swap the current index with start
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            # Swap back (backtrack)
            s[start], s[i] = s[i], s[start]

    backtrack(0)
    return result

def combinations(s: string) -> List:
    result = []
    n = len(s)
    
    def backtrack(start, path):
        result.append("".join(path))
        for i in range(start, n):
            path.append(s[i])
            backtrack(i+1, path)
            path.pop()
    
    backtrack(0, [])
    return result
    
if __name__ == "__main__":
    print(permutations("abc"))
    print(combinations("abc"))

