class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        # Newton's method..
        r = x
        while r * r > x:
            r = (r + x // r) // 2 

        return r
