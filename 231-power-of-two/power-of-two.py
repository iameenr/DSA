class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary_n = bin(n)[2:]

        if binary_n[0] == '0': 
            return False

        for c in binary_n[1:]:
            if c == '1':
                return False

        return True
