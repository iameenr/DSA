class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_window_length = math.inf
        window_sum = 0
        start = 0

        end = 0
        while end in range(len(nums)):
            window_sum += nums[end]

            while window_sum >= target:
                # then shrink the window from left
                # current_wl = (end - start) + 1
                min_window_length = min(min_window_length, (end - start) + 1)

                # shrinking
                window_sum -= nums[start]
                start += 1
            
            end += 1

        if min_window_length == math.inf:
            return 0
        return min_window_length
            
