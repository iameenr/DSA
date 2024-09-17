class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

class MinStack:
    def __init__(self):
        self.min_stack = Stack()
        self.stack = Stack()

    def push(self, val: int) -> None:

        self.stack.push(val)

        if self.min_stack.is_empty() or val <= self.min_stack.peek():
            self.min_stack.push(val)
        
    def pop(self) -> None:
        # popped = self.stack.pop()
        if self.stack.pop() == self.min_stack.peek():
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack.peek()

    def getMin(self) -> int:
        return self.min_stack.peek()
