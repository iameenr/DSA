class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: 
        window_start = 0
        window_sum = 0
        min_window_len = float('inf')
        for window_end, n in enumerate(nums):
            window_sum += n
            while window_sum >= target: 
                # since window_sum > target, we shrink from left till it's not the case
                currwl = (window_end - window_start) + 1
                min_window_len = min(min_window_len, currwl)
                window_sum -= nums[window_start]
                window_start += 1

        return 0 if min_window_len == float('inf') else min_window_len

            
