class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        count = [0]*(len(nums) + 1) 
        result, l, m = 0, 0, 0

        for n in nums:
            count[n] += 1
            if count[n] == 1:
                k -= 1
                if (k < 0):
                    count[nums[m]] = 0
                    m += 1
                    l = m
                    
            if k <= 0:
                while(count[nums[m]] > 1):
                    count[nums[m]] -= 1
                    m += 1
                result += m - l + 1
        return result