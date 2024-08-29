class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = 0
        for n in nums:
            totalsum += n

        ps = 0
        for idx, n in enumerate(nums):
            # leftsum = ps
            # rightsum = totalsum - ps
            if ps == ((totalsum - n) - ps):
                return idx

            ps += n

        return -1
