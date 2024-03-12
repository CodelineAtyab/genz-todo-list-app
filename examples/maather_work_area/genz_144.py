'''
This file contains two classes, Stack and Queue, 
each with methods to perform the required operations.
'''
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Error: Stack is empty"
        popped_item = self.items[-1]
        self.items = self.items[:-1]
        return popped_item

    def peek(self):
        if self.is_empty():
            return "Error: Stack is empty"
        return self.items[-1]

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Error: Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Error: Queue is empty"
        return self.items[0]

q = Queue()
q.enqueue(1)
q.enqueue(4)
q.enqueue(8)
q.dequeue()
q.front()
print(q.front())




