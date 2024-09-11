from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ones[15] = ones[8] + ones[7]
            ones[i] = ones[i // 2] + (i % 2)
        
        return ones
