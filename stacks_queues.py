
class Stack:
    """
    LIFO: Last in first out
    """
    def __init__(self):
        """ insert in the end of the stack """
        self.stack = []
        
    def push(self, element):
        self.stack += [element]
    
    def pop(self):
        """ remove the top (last) element from the stack """
        if len(self.stack) > 0:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp
        else:
            return "No element in stack!"
    
    def peek(self):
        """ take a look at the top (last) element in stack """
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)


def create_stack(list_of_elements):
    stack = Stack()
    for e in list_of_elements:
        stack.push(e)
    return stack
    
    
class Queue:
    """
    FIFO: First in first out
    """
    def __init__(self):
        self.queue = []
    
    def push(self, element):
        self.queue += [element]
        
    def pop(self):
        if len(self.queue) > 0:
            temp = self.queue[0]
            self.queue = self.queue[1:]
            return temp
        else:
            print("No elements in queue!")
    
    def size(self):
        return len(self.queue)
    
        
def create_queue(list_of_elements):
    queue = Queue()
    for e in list_of_elements:
        queue.push(e)
    return queue

    
if __name__ == "__main__":
    print("\nSTACK")
    stack = Stack()
    print(stack.pop())
    
    list_of_elements = [1, 2, 3, 6, 13, 4, 99]
    stack = create_stack(list_of_elements)
    print(stack.peek())
    print(stack.stack)
    stack.pop()
    print(stack.stack)
    print(stack.size())

    print("\nQUEUE")
    queue = create_queue(list_of_elements)
    print(queue.queue)
    print(queue.size())
    queue.pop()
    print(queue.queue)