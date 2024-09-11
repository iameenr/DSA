"""
n steps
1 or 2 steps - at a time

number of permutations to climb to top

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def ways(n):
        #     if n in [0, 1, 2]:
        #         return n
        #     if n in memo:
        #         return memo[n]

        #     memo[n] = ways(n-1) + ways(n-2)
        #     return memo[n]

        if n == 1: return 1
        if n == 2: return 2

        dp = [0]*(n+1)   
        dp[0], dp[1], dp[2] = 0, 1, 2

        for s in range(3, n+1):
            dp[s] = dp[s-1] + dp[s-2]

        return dp[n]
















