class Solution:
    def canJump(self, nums: List[int]) -> bool:

        lennums = len(nums)
        
        max_reach = 0
        for index in range(lennums):
            if index > max_reach:
                return False
            
            reach = index + nums[index]
            max_reach = max(max_reach, reach)
            if max_reach >= (lennums - 1):
                return True

        return False