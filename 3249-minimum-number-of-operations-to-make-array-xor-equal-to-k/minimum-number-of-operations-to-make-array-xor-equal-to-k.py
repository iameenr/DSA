class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        current_xor = reduce(xor, nums)
        # xors with target k to find differing bits
        diff = current_xor ^ k
        
        # Count number of differing bits
        return diff.bit_count()
