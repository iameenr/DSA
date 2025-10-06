class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        # intuition:
        # - if whole array XORs to nonzero, return n
        # - if whole array XORs to zero, 
        #     then removing any 1 element will make xorsum non-zero,
        #     we can return n-1.
        #     but the removed element must not be zero.

        lenn = len(nums)
        xorsum = 0
        for n in nums:
            xorsum = xorsum ^ n
        
        if xorsum != 0:
            return lenn

        for n in nums:
            if n != 0:
                return lenn-1
                
        return 0