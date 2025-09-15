class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lennums = len(nums)
        product_except_self = [1] * lennums

        prefix_product = 1
        for i in range(lennums):
            product_except_self[i] = prefix_product
            prefix_product *= nums[i]
            
        suffix_product = 1
        for i in range(lennums - 1, -1, -1):
            product_except_self[i] *= suffix_product
            suffix_product *= nums[i]

        return product_except_self