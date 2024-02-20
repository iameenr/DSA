class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        inc, dec = None, None
        lennums = len(nums)

        prev = nums[0]
        for i in range(1, lennums):
            n = nums[i]
            if n < prev:
                dec = True
                break
            prev = n

        prev = nums[0]
        for i in range(1, lennums):
            n = nums[i]
            if n > prev:
                inc = True
                break
            prev = n
         
        if inc and dec:
            return False        
        return True

            


