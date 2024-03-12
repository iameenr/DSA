class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        lensat = len(satisfaction)
        max_ltc = 0
        
        for s in range(lensat):
            ltc = 0
            d = 1
            for i in range(s, lensat):
                ltc += d*satisfaction[i]
                d += 1
            max_ltc = max(max_ltc, ltc)

        return max_ltc