class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def get_lower_bound(nums, target):
            low, high = 0, len(nums) - 1
            lower_bound = -1
            while low <= high:
                mid = (low + high) // 2
                if target <= nums[mid]:
                    lower_bound = mid
                    high = mid - 1
                else: # target > nums[mid]
                    low = mid + 1
                
            return lower_bound


        def get_upper_bound(nums, target):
            low, high = 0, len(nums) - 1
            upper_bound = len(nums) # Assuming it's not present
            while low <= high:
                mid = (low + high) // 2
                if target < nums[mid]:
                    upper_bound = mid
                    high = mid - 1
                else: # target > nums[mid]
                    low = mid + 1

            return upper_bound


        lower_bound = get_lower_bound(nums, target)
        upper_bound  = get_upper_bound(nums, target) 

        if lower_bound == -1 or nums[lower_bound] != target:
            return [-1, -1]
        # if lower_bound != -1 and upper_bound == -1:
        #     return [lower_bound, len(nums)-1]

        # now,
        # first_occurence = lower_bound
        # last_occurent = upper_bound - 1
        return [lower_bound, upper_bound - 1]
