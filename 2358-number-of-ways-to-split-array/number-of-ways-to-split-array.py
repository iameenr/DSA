class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0 # result
        lennums = len(nums)

        total_sum = sum(nums)
        
        prefix_sum = 0
        for i in range(0, lennums - 1):
            prefix_sum += nums[i]
            # suffix_sum = (total_sum - prefix_sum)
            if prefix_sum >= (total_sum - prefix_sum):
                valid_splits += 1

        return valid_splits