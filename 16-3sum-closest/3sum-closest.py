import math
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        closest_sum = math.inf  
        lennums = len(nums)
        
        for i in range(lennums - 2): 
            left, right = i + 1, lennums - 1  
            
            while left < right:
                summ = nums[i] + nums[left] + nums[right]  
                
                if abs(target - summ) < abs(target - closest_sum):  # Check if the current sum is closer
                    closest_sum = summ 
                
                if summ < target:  
                    left += 1
                elif summ > target:  
                    right -= 1
                else:
                    return summ  
        
        return closest_sum
