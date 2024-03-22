class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removals = set()
        ls = list(s)
        stack = []
        for i, c in enumerate(ls):
            if c == '(':
                stack.append((')', i))
            if c == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    removals.add(i)

        while stack:
            _, i = stack.pop()
            removals.add(i)

        for i in removals:
            ls[i] = ''

        return "".join(ls)
