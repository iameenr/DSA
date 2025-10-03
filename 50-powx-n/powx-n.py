class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base: float, exponent: int) -> float:
            if exponent == 0:
                return 1.0
            half = fast_pow(base, exponent // 2)
            if exponent % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)
