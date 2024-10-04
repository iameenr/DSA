class Solution:
    def uniquePaths(self, rowlen: int, collen: int) -> int:
        
        def dfs(r, c):
            if r == rowlen - 1 and c == collen - 1:
                return 1
            
            if (r, c) in memo: 
                return memo[(r, c)]

            paths = 0
            # Move right if within bounds
            if r + 1 < rowlen:
                paths += dfs(r + 1, c)
            
            # Move down if within bounds
            if c + 1 < collen:
                paths += dfs(r, c + 1)

            memo[(r, c)] = paths
            return paths

        memo = {}
        paths = dfs(0, 0)
        return paths
