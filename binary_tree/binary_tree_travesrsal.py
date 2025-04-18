from collections import deque
from typing import List
from binary_tree.create_btree import TreeNode, build_balanced_binary_tree, build_binary_tree
    
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
    
    binary_tree = build_balanced_binary_tree(nums)
    # binary_tree = build_binary_tree(nums)
    
    result1 = treeTraversalBfs(binary_tree)
    print(result1)
    result2 = treeTraversalDfs(binary_tree)
    print(result2)