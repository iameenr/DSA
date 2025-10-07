class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def dfs(u):
            nonlocal result
            if result:
                return

            if u == len(pattern) + 1:
                result = ''.join(t)
                return

            for i in range(1, 10):
                if not visited[i]:
                    if u and pattern[u - 1] == 'I' and int(t[-1]) >= i:
                        continue
                    if u and pattern[u - 1] == 'D' and int(t[-1]) <= i:
                        continue
                    visited[i] = True
                    t.append(str(i))
                    dfs(u + 1)
                    visited[i] = False
                    t.pop()

        visited = [False] * 10
        t = []
        result = None
        dfs(0)
        return result