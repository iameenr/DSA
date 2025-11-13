class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0
        for i in range(32):
            temp = 0
            for x in candidates:
                temp = temp + ((x >> i) & 1)
            result = max(result, temp)

        return result