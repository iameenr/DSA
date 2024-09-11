"""
n steps
1 or 2 steps - at a time

number of permutations to climb to top

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def ways(n):
        #     if n in [0, 1, 2]:
        #         return n
        #     if n in memo:
        #         return memo[n]

        #     memo[n] = ways(n-1) + ways(n-2)
        #     return memo[n]

        if n <= 3: 
            return n

        first, second = 1, 2
        for s in range(3, n+1):
            current = first + second            
            first = second
            second = current

        return current
















