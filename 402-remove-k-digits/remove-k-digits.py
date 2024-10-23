from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num: 
            return "0"
        
        stack = deque()
        TOP = -1

        for n in num:
            while k > 0 and stack and stack[TOP] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1

        # Remove trailing zeroes from left
        while stack and stack[0] == '0':
            stack.popleft()

        result = ''.join(stack)

        return result if result else "0"
