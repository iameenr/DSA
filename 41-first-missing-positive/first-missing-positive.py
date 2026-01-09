class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        n = len(nums)
        
        # eliminate all the negative numbers and numbers greater than n
        for index in range(n):
            if nums[index] <= 0 or nums[index] > n:
                nums[index] = n + 1

        # use array as dictionary and mark seen to negative
        for num in nums:
            num = abs(num)
            if num <= n:
                # We subtract by 1 because array indices start at 0
                idx = num - 1 
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]

        # find the first index with non-negative value, that's the answer
        for index in range(n):
            if nums[index] > 0:
                return index + 1  # We add 1 because array indices start at 0
        
        return n + 1