class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        inc, dec = None, None
        lennums = len(nums)

        for i in range(1, lennums):
            if nums[i] < nums[i-1]:
                dec = True
                break


        for i in range(1, lennums):
            if nums[i] > nums[i-1]:
                inc = True
                break
         
        if inc and dec:
            return False        
        return True

            


