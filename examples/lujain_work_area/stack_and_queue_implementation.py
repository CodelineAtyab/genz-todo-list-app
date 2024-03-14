class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Error: Stack is empty. Cannot pop."
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Error: Stack is empty. Cannot peek."
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Error: Queue is empty. Cannot dequeue."
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Error: Queue is empty. Cannot front."
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Peek:", stack.peek())

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.items)
print("Dequeue:", queue.dequeue())
print("Front:", queue.front())