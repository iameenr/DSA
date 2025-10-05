class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxreach = 0
        for idx, jump in enumerate(nums):
            if idx > maxreach:
                return False
            maxreach = max(maxreach, (idx + jump))

        return True
