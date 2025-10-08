class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxx = result = 0
        for x in nums:
            maxx = maxx | x

        def dfs(i, t):
            nonlocal maxx, result
            if i == len(nums):
                if t == maxx:
                    result += 1
                return
            dfs(i + 1, t)
            dfs(i + 1, t | nums[i])

        dfs(0, 0)
        return result