class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(num + nums[n - index - 1] for index, num in enumerate(nums[: n >> 1]))