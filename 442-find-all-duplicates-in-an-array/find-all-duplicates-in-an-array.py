class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for x in nums:
            x = abs(x)
            if nums[x-1] < 0:
                result.append(x)
            nums[x-1] *= -1
             
        return result