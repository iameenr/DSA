class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lennums = len(nums)-1
        low, high = 0, lennums

        while low <= high:

            mid = (low+high)//2

            if (mid == 0 or nums[mid-1] < nums[mid]) and \
               (mid == lennums or nums[mid] > nums[mid+1]):
               return mid
            # if on increasing curve, search right:
            elif mid < lennums and nums[mid] < nums[mid+1]:
                low = mid+1
            # On decreasing curve, so search right:
            else:
                high = mid-1

        return -1