class Solution:
    def rob(self, profit: List[int]) -> int:
        houses = len(profit)
        if houses == 1: return profit[0]
        if houses == 2: return max(profit[0], profit[1])
        
        first, second = profit[0], max(profit[0], profit[1])
        for house in range(2, houses):
            current = max(first + profit[house], second)
            first = second
            second = current

        return current