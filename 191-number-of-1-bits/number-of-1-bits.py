class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        
        while n > 0:
            if n % 2 == 1:
                hamming_weight += 1
            n = n // 2

        return hamming_weight