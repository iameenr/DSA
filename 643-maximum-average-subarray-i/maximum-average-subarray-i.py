class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        
        max_average = window_sum / k
        
        window_start = 0 
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[window_start] + nums[i]
            
            window_start += 1
            
            curravg = window_sum / k
            max_average = max(max_average, curravg)

        return max_average