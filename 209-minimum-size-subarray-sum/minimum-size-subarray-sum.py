import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        window = 0
        start = 0
        minwl = math.inf
        for end, n in enumerate(nums):
            window += n

            # shrink from left
            while window >= target:
                minwl = min(minwl, (end - start) + 1)
                window -= nums[start]
                start += 1

        if minwl == math.inf: return 0
        return minwl
