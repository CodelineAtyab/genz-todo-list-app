class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack)
print("Pop:", stack.pop())
print("Stack after pop:", stack)
print("Peek:", stack.peek())
print("Stack after peek:", stack)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("\nQueue after enqueues:", queue)
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue)
print("Front:", queue.front())
print("Queue after front:", queue)