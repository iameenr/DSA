class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        sum of range of numbers = n*(n+1)/2
        """
        range_ = len(nums)
        range_sum = range_*(range_+1) // 2
        input_array_sum = 0
        for n in nums:
            input_array_sum += n

        missing_number = range_sum - input_array_sum
        return missing_number
