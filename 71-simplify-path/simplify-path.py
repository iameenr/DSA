class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()


class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = Stack()
        for dirr in path.split('/'):
            if dirr == "..": 
                stack.pop()

            elif dirr and dirr != '.':
                stack.push(dirr)

        # print(stack)
        return '/' + "/".join(stack.stack)