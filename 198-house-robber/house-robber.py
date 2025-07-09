class Solution:
    def rob(self, profit: List[int]) -> int:
        """MEMOIZATION"""
        # n = len(profit)
        # if n == 1:
        #     return profit[0]
        # if n == 2:
        #     return max(profit[0], profit[1])
        
        # dp = [0] * n
        # dp[0] = profit[0]
        # dp[1] = max(profit[0], profit[1])
        
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2] + profit[i])
        
        # return dp[n-1]

        """DP"""
        houses = len(profit)
        if houses == 1: return profit[0]
        if houses == 2: return max(profit[0], profit[1])
        
        first, second = profit[0], max(profit[0], profit[1])
        for house in range(2, houses):
            current = max(first + profit[house], second)
            first = second
            second = current

        return current