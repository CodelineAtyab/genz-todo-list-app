# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def front(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]
    
# Stack Example
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)  
print(stack.pop())
print(stack.peek())  
print(stack.stack)  

# Queue Example
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue) 
print(queue.dequeue())  
print(queue.front())  
print(queue.queue)  