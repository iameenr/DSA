class Solution:
    def checkValidString(self, s: str) -> bool:
        # store the indices of '('
        stack = []
        # store the indices of '*'
        star = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append( idx )
                
            elif char == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
                    
            else:
                star.append( idx )
        
        
        # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
        while stack and star:
            if stack[-1] > star[-1]:
                return False
        
            stack.pop()
            star.pop()
        
        
        # Accept when stack is empty, which means all braces are paired
        # Reject, otherwise.
        return len(stack) == 0
                