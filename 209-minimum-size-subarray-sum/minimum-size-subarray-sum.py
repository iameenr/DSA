import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        min_window_length = math.inf
        start = 0
        
        for end, n in enumerate(nums):
            window_sum += n

            # shrink from left
            while window_sum >= target:
                min_window_length = min(min_window_length, (end - start) + 1)
                window_sum -= nums[start]
                start += 1

        if min_window_length == math.inf: return 0
        return min_window_length