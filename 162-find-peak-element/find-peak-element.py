class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        lennums = len(nums)-1
        for i, n in enumerate(nums):
            if (i == 0 or nums[i-1] < nums[i])  and (i == lennums or nums[i] > nums[i+1]):
                return i  