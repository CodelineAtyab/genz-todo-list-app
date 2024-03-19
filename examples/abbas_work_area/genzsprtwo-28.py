"""
Stack and Queue solution, LIFO & FIFO
"""


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()  # pops last value

    def push(self, num):
        self.stack.append(num)  # pushes numbers to stack

    def peak(self):  # returns peak value
        return self.stack[-1]


class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueu(self, num):  # append queue
        self.queue.append(num)
    
    def dequeue(self):  # remove first in from queue
        if not self.queue:
            return "List is empty"
        return self.queue.pop(0)
    
    def next(self):  # shows whats left in queue
        return self.queue


"""
stack related print and push lines of code
"""


stack_func = Stack()
stack_func.push(1)
stack_func.push(2)
print(f"stack: {stack_func.stack}")
print(f"pop: {stack_func.pop()}")
print(f"Peak: {stack_func.peak()}")
print(f"update: {stack_func.stack}")


"""
Queue related enqueue and print lines
"""


queue_func = Queue()
queue_func.enqueu(1)
queue_func.enqueu(2)
print(f"queue: {queue_func.queue}")
print(f"Dequeue: {queue_func.dequeue()}")
print(f"next: {queue_func.next()}")
