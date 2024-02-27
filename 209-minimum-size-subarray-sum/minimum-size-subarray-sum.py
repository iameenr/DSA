import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        window_sum, min_window_length = 0, math.inf
        lennums = len(nums)
        start, end = 0, 0
        
        while end < lennums:
            window_sum += nums[end]

            # shrink from left
            while window_sum >= target:
                min_window_length = min(min_window_length, (end - start) + 1)
                window_sum -= nums[start]
                start += 1
            end += 1

        if min_window_length == math.inf: return 0
        return min_window_length
