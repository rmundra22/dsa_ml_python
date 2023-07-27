class LNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = LNode(data)
        
    def traverse_and_print(self):
        temp = self.head
        print("\nTraversing and printing linked list")
        while temp:
            print(temp.data)
            temp = temp.next
        print("done\n")
      
    def insert_at_end(self, element):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = LNode(element)
        
    def insert_at_beginning(self, element):
        e = LNode(element)
        e.next = self.head
        self.head = e
        
    def insert_before_element(self, reference_element, element):
        e = LNode(element)
        temp = self.head
        
        if temp.data == reference_element:
            temp2 = temp.next
            self.head.next = e
            e.next = temp2
            
        while temp.next:
            if temp.next.data == reference_element:
                temp2 = temp.next
                temp.next = e
                e.next = temp2 
            temp = temp.next
            
        return
    
    def insert_after_element(self, reference_element, element):
        e = LNode(element)
        temp = self.head
            
        while temp:
            if temp.data == reference_element:
                temp2 = temp.next
                temp.next = e
                e.next = temp2 
            temp = temp.next
            
        return
    
    def remove_element(self, element):
        temp = self.head
        if temp.data == element:
            self.head = self.head.next
            return
            
        while temp.next:
            if temp.next.data == element:
                temp.next = temp.next.next
                return
            temp = temp.next
            
        return
    
      
def create_linked_list(elements):
    listA = LinkedList(elements[0])
    
    temp = listA.head
    for e in elements[1:]:
        node = LNode(e)
        temp.next = node
        temp = node
    
    return listA

# Create the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Define the push method to add elements		
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    # Define the insert method to insert the element		
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    # Define the method to print the linked list 
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.push(12)
    dllist.push(8)
    dllist.push(62)
    dllist.insert(dllist.head.next, 13)
    dllist.listprint(dllist.head)
    
    # 3 elements as nodes in linked list
    e1 = LNode("Mon")
    e2 = LNode("Tue")
    e3 = LNode("Wed")

    # # create a linked list
    # list1 = LinkedList()
    # list1.headval = e1

    # # Link first Node to second node
    # list1.headval.nextval = e2

    # # Link second Node to third node
    # e2.nextval = e3
    
    # create linked list
    list_of_elements = [1, 42, 12, 4, 3, 35, 6]
    linked_list = create_linked_list(list_of_elements)
    linked_list.insert_at_end(99)
    linked_list.remove_element(1)
    linked_list.remove_element(12)
    linked_list.remove_element(3)
    linked_list.insert_at_beginning(100)
    linked_list.insert_before_element(6, 1008)
    linked_list.insert_after_element(6, 64)
    # element will only be inserted if reference element is present
    linked_list.insert_after_element(16, 64)
    
    linked_list.traverse_and_print()
    