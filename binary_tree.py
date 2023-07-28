class BinaryTree:
    """
    For tree with height 'h' i.e., 3 levels
    - Maximum nodes at level 'h' will be 2^h
    - Maximum nodes in the entire tree will be 2^(h+1)-1
    - In perfect binary tree, internal nodes = num_of_leaves - 1
    - Height of Tree: H, Number of Nodes: N then H = floor(logN with base2)
    """
    
    def __init__(self, element):
        """ insert, search and remove: O(log(n)) """
        self.data = element
        self.right = None
        self.left = None
    
    
    def insert(self, element):
        if self.data:
            if element <= self.data:
                if self.left:
                    self.left.insert(element)
                else:
                    self.left = BinaryTree(element)
            elif element > self.data:
                if self.right:
                    self.right.insert(element)
                else:
                    self.right = BinaryTree(element)  
        else:
            self.data = element
            
            
    def print_tree(self):
        """ printing the tree in in-order"""
        if self.left:
            self.left.print_tree()
            
        print(self.data)
        
        if self.right:
            self.right.print_tree()

            
    def search(self, element):
        if self.data == element:
            print('key found!')
            return
        elif self.data < element and self.right:
            return self.right.search(element)
        elif self.left:
            return self.left.search(element)
        print("key not found!")
    
    
    def _swap_and_drop(self, A, element):
        max_element = A
        while max_element.right:
            max_element = max_element.right
        
        temp = A.data
        A.data = max_element.data
        max_element.data = temp
        
        self.max_element.remove(element)
        
    
    def remove(self, A, element):
        """incomplete"""
        if self.data == element:
            if self.left is None:
                if self.right:
                    self.data = self.right.data
                    self.right = self.right.right
                    self.left = self.right.left
                else:
                    self.data = None
                    return None
            elif self.right is None:
                if self.left:
                    self.data = self.left.data
                    self.right = self.left.right
                    self.left = self.left.left
            else:
                self._swap_and_drop(self.left, element)                
        elif self.data < element:
            self.right.remove(self.right, element)
        else:
            self.left.remove(self.left, element)
    
    
    def traversal(self, root, type="in-order"):
        tree_elements = []
        
        if root:
            if type == "in-order":
                tree_elements = self.traversal(root.left, type)
                tree_elements.append(root.data)
                tree_elements += self.traversal(root.right, type)
            elif type == "pre-order":
                tree_elements.append(root.data)
                tree_elements += self.traversal(root.left, type)
                tree_elements += self.traversal(root.right, type)
            elif type == "post-order":
                tree_elements = self.traversal(root.left, type)
                tree_elements += self.traversal(root.right, type)
                tree_elements.append(root.data)
        
        return tree_elements
        

def create_binary_tree(L):
    start_node = L[0]
    btree = BinaryTree(start_node)
    
    for element in L[1:]:
        btree.insert(element)
        
    return btree  
            

if __name__ == "__main__":
    L = [2, 41, 0, 4, 4, 82]
    btree = create_binary_tree(L)
    print("Printing Tree")
    btree.print_tree()
    btree.search(2)
    btree.search(82)
    btree.search(122) 
    
    L = [12, 5, 3, 1, 7, 9, 8, 11, 15, 13, 14, 17, 20, 18]
    
    # remove: case 1
    btree = create_binary_tree(L)
    btree.remove(btree, 7)
    print("Printing Tree")
    btree.print_tree()
    
    # remove: case 2 
    # btree = create_binary_tree(L)
    # btree.remove(btree, 17)
    # print("Printing Tree")
    # btree.print_tree()
    
    # remove: case 3
    # btree = create_binary_tree(L)
    # btree.remove(btree, 15)
    # print("Printing Tree")
    # btree.print_tree()
    
    # remove: case 4
    # btree = create_binary_tree(L)
    # btree.remove(btree, 12)
    # print("Printing Tree")
    # btree.print_tree()
    
    # traversal: 3 types
    # btree = create_binary_tree(L)
    # print("Printing Tree")
    # print(btree.traversal(btree, "in-order"))
    # print(btree.traversal(btree, "pre-order"))
    # print(btree.traversal(btree, "post-order"))
    