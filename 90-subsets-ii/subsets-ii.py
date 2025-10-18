class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start_idx, t):
            result.append(t[:]) 
            for i in range(start_idx, len(nums)):
                if i != start_idx and nums[i] == nums[i - 1]:
                    continue
                t.append(nums[i])
                dfs(i + 1, t)
                t.pop()

        result = []
        nums.sort()
        dfs(0, [])
        return result