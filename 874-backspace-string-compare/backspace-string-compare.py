class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def parse(string: str) -> str:
            result = []
            for c in string:
                if c == '#':
                    if result:
                        result.pop()
                else:
                    result.append(c)
            return "".join(result)

        return parse(s) == parse(t)
