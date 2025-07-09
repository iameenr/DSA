class Solution:
    def rob(self, profit: List[int]) -> int:
        memo = {}

        def _rob(house):
            if house == 0:
                return profit[house]
            if house == 1:
                return max(profit[0], profit[1])
            if house in memo:
                return memo[house]
                
            rob_this_house = _rob(house-2) + profit[house]
            dont_rob_this_house = _rob(house-1)
            max_profit = max(rob_this_house, dont_rob_this_house)
            memo[house] = max_profit
            return max_profit

        return _rob(len(profit)-1)