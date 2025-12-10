class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        max_subarray_sum = float('-inf')
        for n in nums:
            summ += n
            max_subarray_sum = max(max_subarray_sum, summ)
            if summ < 0:
                summ = 0
                continue

        return max_subarray_sum