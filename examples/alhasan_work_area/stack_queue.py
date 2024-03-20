"""

An implementation of two classes;
one class is responsible for doing stack operations (push, pop, peek)
the other class is responsible for doing queue operations (enqueue, dequeue, front)

"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        elif len(self.stack) == 0:
            return "Cannot perform the operation, the stack is empty"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        elif len(self.stack) == 0:
            return "Cannot perform the operation, the stack is empty"


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, number):
        self.queue.append(number)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        elif len(self.queue) == 0:
            return "Cannot perform the operation, the queue is empty"

    def front(self):
        if self.queue:
            return self.queue[0]
        elif len(self.queue) == 0:
            return "Cannot perform the operation, the queue is empty"


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print("Push: 1, 2, 3", ",", "( " "Stack:", stack1.stack, ")")
print("Pop:", stack1.pop(), ",", "( " "Stack:", stack1.stack, ")")
print("Current Stack:", stack1.stack, ",", "Peek:", stack1.peek())

queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
print("Enqueue: 1, 2, 3", ",", "( " "Queue:", queue1.queue, ")")
print("Dequeue:", queue1.dequeue(), ",", "( " "Queue:", queue1.queue, ")")
print("Current Queue:", queue1.queue, ",", "Front:", queue1.front())
