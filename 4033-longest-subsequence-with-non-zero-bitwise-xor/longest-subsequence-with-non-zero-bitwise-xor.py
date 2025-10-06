class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0
        for x in nums:
            xor_all ^= x
        
        if xor_all != 0:
            return n

        # xor_all == 0
        if all(x == 0 for x in nums):
            return 0
            
        return n - 1
