class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        positive_pointer = 0  # Index for placing positive elements 
        negative_pointer = 1  # Index for placing negative elements

        for num in nums:
            if num > 0:
                result[positive_pointer] = num
                positive_pointer += 2
            else:
                result[negative_pointer] = num
                negative_pointer += 2

        return result
