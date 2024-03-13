class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        range_sum  = n*(n+1) / 2
        """
        if n == 1: return 1
        
        rs = (n*(n+1)) // 2

        for i in range(n):
            crs = (i*(i+1)) // 2
            if crs == (i + (rs - crs)):
                return i

        return -1