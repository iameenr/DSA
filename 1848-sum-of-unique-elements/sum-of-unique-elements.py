from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        seen = defaultdict(int)
        sum_of_unique = 0
        for n in nums:
            seen[n] += 1
        for n, c in seen.items():
            if c == 1:
                sum_of_unique += n

        return sum_of_unique