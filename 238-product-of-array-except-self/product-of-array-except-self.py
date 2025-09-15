class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lennums = len(nums)
        if lennums == 0: 
            return []

        prefix_product_list = [1] * lennums
        suffix_product_list = [1] * lennums
        product_except_self = [1] * lennums

        running_product = 1
        for i in range(lennums):
            prefix_product_list[i] = running_product
            running_product *= nums[i]
            
        running_product = 1
        for i in range(lennums - 1, -1, -1):
            suffix_product_list[i] = running_product
            running_product *= nums[i]

        for i in range(0, lennums):
            product_except_self[i] = prefix_product_list[i] * suffix_product_list[i]

        return product_except_self