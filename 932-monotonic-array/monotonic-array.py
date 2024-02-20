class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        inc, dec = None, None

        prev = nums[0]
        for n in nums[1:]:
            if n < prev:
                dec = True
                break
            prev = n

        prev = nums[0]
        for n in nums[1:]:
            if n > prev:
                inc = True
                break
            prev = n
         
        if inc and dec:
            return False        
        return True

            


