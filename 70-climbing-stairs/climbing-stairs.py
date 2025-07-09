class Solution:
    def climbStairs(self, n: int) -> int:
        # def _climb(n, memo):
        #     if n <= 3:
        #         return n

        #     if n in memo:
        #         return memo[n]

        #     take_one_step  = self.climbStairs(n-1)
        #     take_two_steps = self.climbStairs(n-2)
        #     memo[n] = take_one_step + take_two_steps
        #     return memo[n]

        # memo = {} # 4 : 5 ways
        # return _climb(n, memo)

        if n <= 3:
            return n

        # assign base case
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3


        # rewrite recurrence as dp array
        # f(n) = f(n-1) + f(n-2)
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]














