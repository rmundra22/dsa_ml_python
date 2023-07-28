import heapq

# Heap is a special tree structure in which each parent node is less than or equal 
# to its child node. Then it is called a Min Heap. If each parent node is greater 
# than or equal to its child node then it is called a max heap. It is very useful 
# is implementing priority queues where the queue item with higher weightage is 
# given more priority in processing.

# Complete Binary Tree Types
# A. Perfect BT
# - All leaves at all levels are present

# B. Almost Perfect BT
# - Not all leaves are present as PBT
# - Leaves at same level should be filled from left to right
# - Leaves should only be at last or 2nd last level

# Property of Heaps 
# - Tree Data Structure
# - Complete Binary Tree
# - Follows Heap Property (Min or Max heap)

# Types of Heap
# - MIN HEAP: minimum element at root node and same for all sub-trees
# -- all elements are in increasing order in a list than that will result in min heap
# - MAX HEAP: maximum element at root node and same for all sub-trees
# -- all elements are in decreasing order in a list than that will result in max heap

# Tricks
# If parent is at index 'i' then left child will be at '2i +1' and right child will be at '2i+2'
# If child node is 'j' than parent node will be 'ceiling[i/2] - 1'


if __name__ == "__main__":
    H = [21,1,45,78,3,5]
    # Use heapify to rearrange the elements (MIN HEAP)
    heapq.heapify(H)
    print(H)
    
    # Add element
    heapq.heappush(H,8)
    print(H)
    
    # Remove element from the heap
    heapq.heappop(H)
    print(H)
    
    # Replace an element: 
    # replaces the smallest data element with a new value supplied in the function.
    heapq.heapreplace(H,6)
    print(H)