class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        result = 0
        lenpiles = len(piles)
        for second_largest in range(lenpiles // 3, lenpiles, 2):
            result += piles[second_largest]
        
        return result