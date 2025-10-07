class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(t):
            if len(t) == n:
                result.append(t)
                return

            for char_ in 'abc':
                if t and t[-1] == char_:
                    continue
                dfs(t + char_)

        result = []
        dfs('')
        return '' if len(result) < k else result[k - 1]