from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws = 0
        for i in range(k):
            ws += nums[i]
        
        maxavg = ws / k
        wst = 0 
        for i in range(k, len(nums)):
            ws = ws - nums[wst] + nums[i]
            
            wst += 1
            
            curravg = ws / k
            maxavg = max(maxavg, curravg)

        return maxavg