class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0,1,2]: return n

        one = 1
        two = 2
        for i in range(3, n+1):
            curr = one + two
            one = two
            two = curr
        return curr