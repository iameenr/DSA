class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        max_band_length = 0
        for n in nums:
            if n-1 in numset: 
                continue

            # start of a band
            band_length = 0
            while (n + band_length) in numset:
                band_length += 1

            max_band_length = max(max_band_length, band_length)

        return max_band_length