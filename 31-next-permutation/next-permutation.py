class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Find the break point.
        smallest = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                smallest = i
                break
        
        if smallest == -1:
            nums.reverse()
            return

        # 2. find the smallest ele in the rest of the array
        for i in range(len(nums)-1, smallest - 1, -1):
            if nums[i] > nums[smallest]:
                second_smallest = i
                break
        
        # 3. swap smallest and second_smallest, and return reverse of rest
        nums[smallest], nums[second_smallest] = nums[second_smallest], nums[smallest]

        nums[smallest+1:] = reversed(nums[smallest+1:])
        return