"""
A program to create stack and queue functions
"""

class Stack():
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def pop(self):
        if not self.empty():
             self.elements = self.elements[:-1]
             pop = self.elements[-1]
             return pop
        return "Sorry, the stack is empty"
    
    def push(self, element):
        self.elements.append(element)
    
    def peek(self):
        if not self.empty():
            return self.elements[-1]
        return "Sorry, the stack is empty"
    
class Queue():
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if not self.elements:
            first = self.elements[0]
            self.elements = self.elements[1::] 
            return first
        return "Sorry, the queue is empty"
    
    def front(self):
        if not self.empty():
            return self.elements[0]
        return "Sorry, the queue is empty"
    
queue = Queue()
queue.enqueue(1)
print(queue.elements)

stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.push(3)
print(stack.elements)
print(stack.peek())