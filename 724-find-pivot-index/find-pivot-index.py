class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            total_sum += n

        prefix_sum = 0
        for idx, n in enumerate(nums):
            # leftsum = prefix_sum
            # rightsum = total_sum - prefix_sum
            if prefix_sum == ((total_sum - n) - prefix_sum):
                return idx

            prefix_sum += n

        return -1
