class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(index, memo):
            if index >= len(nums):
                return 0

            if index in memo:
                return memo[index]

            rob_current = _rob(index+2, memo) + nums[index]
            rob_next = _rob(index+1, memo)

            max_profit = max(rob_current, rob_next)

            memo[index] = max_profit
            return max_profit

        memo = {}
        return _rob(0, memo)
        