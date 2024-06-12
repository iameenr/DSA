class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        lennums = len(nums)
        
        if lennums == 0:
            return result
        
        first_item = nums[0]
        SEEING_RANGE = False
        
        for i in range(1, lennums):
            curr, prev = nums[i], nums[i - 1]

            if curr == prev + 1:
                SEEING_RANGE = True
            else:
                if SEEING_RANGE:
                    result.append("{}->{}".format(first_item, prev))
                else:
                    result.append("{}".format(first_item))
                    
                SEEING_RANGE = False
                first_item = curr
        
        # Add the last range or number
        if SEEING_RANGE:
            result.append("{}->{}".format(first_item, nums[-1]))
        else:
            result.append("{}".format(first_item))
        
        return result
