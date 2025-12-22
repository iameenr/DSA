class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for index, value in enumerate(nums):
            if value == 0:
                if index + 2 >= len(nums):
                    return -1

                nums[index + 1] ^= 1
                nums[index + 2] ^= 1
                operations += 1
                
        return operations
