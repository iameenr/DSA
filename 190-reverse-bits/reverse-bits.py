class Solution:
    def reverseBits(self, n: int) -> int:
        
        rev = []
        for i in range(32):
            if n % 2 == 1:
                rev.append("1")
            else:
                rev.append("0")
            n = n // 2

        return int("".join(rev), 2)
        