class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        current_xor = 0
        for num in nums:
            current_xor ^= num

        # xors with target k to find differing bits
        diff = current_xor ^ k
        
        # Count number of differing bits
        return diff.bit_count()
