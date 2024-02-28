class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_index = len(nums)-1
        maxreach = 0

        for index, jump in enumerate(nums):
            if index > maxreach: 
                return False
            maxreach = max(maxreach, (index + jump))
            if maxreach >= end_index:
                return True

        return False