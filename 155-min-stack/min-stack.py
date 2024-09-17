class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.is_not_empty() else None
    
    def peek(self):
        return self.stack[-1] if self.is_not_empty() else None

    def is_not_empty(self):
        if self.stack:
            return True
        return False


class MinStack:
    def __init__(self):
        self.min_stack = Stack()
        self.min_stack.push(math.inf)
        self.stack = Stack()

    def push(self, val: int) -> None:
        if self.min_stack.is_not_empty() and val <= self.min_stack.peek():
                self.min_stack.push(val)
        self.stack.push(val)

    def pop(self) -> None:
        if self.stack.is_not_empty():
            if self.stack.pop() == self.min_stack.peek():
                self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack.peek()

    def getMin(self) -> int:
        return self.min_stack.peek()
