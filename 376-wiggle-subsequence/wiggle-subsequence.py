class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        numslen = len(nums)
        ans = 1
        inc = None

        for i in range(1, numslen):
            prev, curr = nums[i-1], nums[i]
            
            if curr > prev and inc != True:
                ans += 1
                inc = True

            if curr < prev and inc != False:
                ans += 1
                inc = False

        return ans