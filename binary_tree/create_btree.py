from binary_tree.binary_tree_travesrsal import treeTraversalBfs, treeTraversalDfs

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def build_balanced_binary_tree(lst):
    "using bfs traversal to fill out btree"
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
        
def build_binary_tree(lst):
    "using bfs traversal to fill out btree"
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        current = queue.pop(0)

        # Left child
        if i < len(lst):
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(lst):
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, None, 8, 9, 10]
    
    binary_tree = build_balanced_binary_tree(nums)
    # binary_tree = build_binary_tree(nums)
    
    result1 = treeTraversalBfs(binary_tree)
    print(result1)
    result2 = treeTraversalDfs(binary_tree)
    print(result2)