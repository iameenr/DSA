from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        lennums = len(nums)
        
        for i in range(lennums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element
            
            left, right = i + 1, lennums - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for the second element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for the third element
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
