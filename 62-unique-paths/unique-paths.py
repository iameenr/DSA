class Solution:
    def uniquePaths(self, rowlen: int, collen: int) -> int:
        """ 
        """     
        dp = [[1]*collen for _ in range(rowlen)]

        for c in range(collen-2, -1, -1):
            for r in range(rowlen-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]

        
        return dp[0][0]