class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        for i, j in pairwise([0] + pref):
            result.append(i ^ j)
        return result