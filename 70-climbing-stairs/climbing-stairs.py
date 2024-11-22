class Solution:
    def climbStairs(self, num_steps: int) -> int:
        if num_steps <= 3:
            return num_steps

        first, second = 1, 2
        for current in range(3, num_steps+1):
            current = first + second
            first = second
            second = current

        return current