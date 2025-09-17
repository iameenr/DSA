class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        lennums = len(nums)
        valid_splits = 0
        ts = 0
        for n in nums:
            ts += n
        
        ps = 0
        for i in range(0, lennums - 1):
            ps += nums[i]
            # sum_of_rest = (ts - ps)
            if ps >= (ts - ps):
                valid_splits += 1

        return valid_splits