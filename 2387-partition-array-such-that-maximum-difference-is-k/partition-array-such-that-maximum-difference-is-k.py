class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        result, a = 1, nums[0]
        for b in nums:
            if b - a > k:
                a = b
                result += 1
        return result