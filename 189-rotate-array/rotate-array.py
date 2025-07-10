class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n  # Handle cases where k > n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1: Reverse the entire array
        reverse(0, n - 1)

        # 2: Reverse the first k elements
        reverse(0, k - 1)

        # 3: Reverse the rest
        reverse(k, n - 1)



        """O(k)"""
        # n = len(nums)
        # k = k % n  # This handles cases where k is larger than n
        
        # # If k is 0, no changes are needed
        # if k == 0:
        #     return

        # temp = nums[-k:]  
        
        # # Shift the rest of the elements to the right by k positions
        # for i in range(n-1, k-1, -1):
        #     nums[i] = nums[i-k]

        # nums[:k] = temp
