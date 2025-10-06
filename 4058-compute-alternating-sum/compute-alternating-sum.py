class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        lennums = len(nums) - 1

        asum = 0
        for i in range(0, lennums + 1, 2):
            asum += nums[i]
        
        ssum = 0
        for i in range(1, lennums+1, 2):
            ssum += nums[i]

        return asum - ssum