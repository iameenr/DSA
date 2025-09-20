class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            
            # If the character is already in our result stack, we can skip it.
            # Its current position in the stack is the best it can be.
            if char in seen:
                continue
            
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)