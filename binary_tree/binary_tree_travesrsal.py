from typing import List
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def build_binary_tree(lst):
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        current = queue.pop(0)

        # Left child
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root

    
# for odd level add right-most node and for even add left-most node to the answer
def treeTraversalBfs(root: TreeNode) -> List[int]:
    queue = deque([root])
    result = []
   
    while queue:
        node = queue.popleft()
        result.append(node.data)
            
        if node.left:
            queue.append(node.left)
            
        if node.right:
            queue.append(node.right)
        
    return result

def treeTraversalDfs(root: TreeNode) -> List[int]:
    stack = deque([root])
    result = []
   
    while stack:
        node = stack.pop()
        result.append(node.data)
            
        if node.left:
            stack.append(node.left)
            
        if node.right:
            stack.append(node.right)
        
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, None, 8, 9, 10]
    binary_tree = build_binary_tree(nums)
    print(binary_tree)
    
    result1 = treeTraversalBfs(binary_tree)
    print(result1)
    result2 = treeTraversalDfs(binary_tree)
    print(result2)