class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        freq = {}
        n = len(nums)

        start = 0
        for end in range(n):
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            
            if freq[nums[end]] > k:
                while nums[start] != nums[end]:
                    freq[nums[start]] -= 1
                    start += 1
                freq[nums[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans