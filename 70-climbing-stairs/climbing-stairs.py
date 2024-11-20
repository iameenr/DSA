class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n 

        first, second = 1, 2
        for _ in range(3, n+1):
            current = first + second
            first = second
            second = current

        return current
















