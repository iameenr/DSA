class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        for dirr in path.split('/'):
            if dirr == "..": 
                if stack: stack.pop()

            elif dirr and dirr != '.':
                stack.append(dirr)

        # print(stack)
        return '/' + "/".join(stack)