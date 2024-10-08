class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1 or n == 2): 
            return n

        first, second, current = 1, 2, 0
        for steps in range(3, n+1):
            current = first + second
            first = second
            second = current
            
        return current
        