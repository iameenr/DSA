class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                
        return left + 1