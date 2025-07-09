class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for current_target_amount in range(1, amount + 1):
            for coin in coins:
                if current_target_amount - coin >= 0 and \
                   dp[current_target_amount - coin] != float('inf'):
                    dp[current_target_amount] = min(
                        dp[current_target_amount],
                        dp[current_target_amount - coin] + 1
                    )

        return dp[amount] if dp[amount] != float('inf') else -1
