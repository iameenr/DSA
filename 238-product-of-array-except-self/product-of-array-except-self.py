class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lennums = len(nums)
        result=[1]*lennums

        prefix_product = 1
        post = 1
        for i in range(lennums):
            result[i] *= prefix_product
            prefix_product = prefix_product*nums[i]
            result[lennums-i-1] *= post
            post = post*nums[lennums-i-1]

        return result