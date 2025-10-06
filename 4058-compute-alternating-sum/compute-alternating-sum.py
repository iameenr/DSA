class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        def altsum(index):
            altsum_ = 0
            for i in range(index, lennums + 1, 2):
                altsum_ += nums[i]
            return altsum_

        lennums = len(nums) - 1
        return altsum(0) - altsum(1)