class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(subarray):
            subarray.sort()
            diff = subarray[1] - subarray[0]
            
            for i in range(2, len(subarray)):
                if subarray[i] - subarray[i - 1] != diff:
                    return False
                
            return True
        
        result = []
        for i in range(len(l)):
            subarray = nums[l[i] : r[i] + 1]
            result.append(is_arithmetic(subarray))
        
        return result