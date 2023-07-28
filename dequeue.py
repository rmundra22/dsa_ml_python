
class Dequeue:
    """
    Double-ended queue, or deque, supports adding and removing elements from 
    either end. The more commonly used stacks and queues are degenerate forms 
    of deques, where the inputs and outputs are restricted to a single end
    """
    def __init__(self):
        self.dequeue = []
    
    def append(self, element):
        self.dequeue += [element]
    
    def append_left(self, element):
        self.dequeue = [element] + self.dequeue
    
    def pop(self):
        """ remove the top (last) element from the stack """
        if len(self.dequeue) > 0:
            temp = self.dequeue[-1]
            self.dequeue = self.dequeue[:-1]
            return temp
        else:
            return "No element in stack!"
    
    def pop_left(self):
        if len(self.dequeue) > 0:
            temp = self.dequeue[0]
            self.dequeue = self.dequeue[1:]
            return temp
        else:
            print("No elements in queue!")
    
    def size(self):
        return len(self.dequeue)
    
    
if __name__ == "__main__":
    list_of_elementsA = [1, 2, 3, 6] 
    list_of_elementsB = [13, 4, 99]
    
    dequeue = Dequeue()
    for e in list_of_elementsA:
        dequeue.append(e)
    
    print(dequeue.dequeue)
    
    for e in list_of_elementsB:
        dequeue.append_left(e)
    
    print(dequeue.dequeue)
        
    dequeue.pop()
    print(dequeue.dequeue)
    dequeue.pop_left()
    print(dequeue.dequeue)
    
    print(dequeue.size())