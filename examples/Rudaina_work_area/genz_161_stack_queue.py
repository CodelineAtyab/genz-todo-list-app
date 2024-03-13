
"""
Stack and Queue
"""


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def push(self, num):
        self.stack.append(num)

    def peek(self):
        if self.stack:
            return self.stack[-1]


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def front(self):
        if self.queue:
            return self.queue[0]


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(f'Push 1, 2, 3: {stack1.stack}')
print(f'Pop: Returns -> {stack1.pop()}')
print(f'Updated Stack: {stack1.stack}')
print(f'Peek: Returns -> {stack1.peek()}\n')

queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
print(f'Enqueue 1,2,3: {queue1.queue} ')
print(f'Dequeue: Returns -> {queue1.dequeue()}')
print(f'Front: Returns -> {queue1.front()}')
