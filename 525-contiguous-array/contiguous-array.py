class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        seen = {0: -1}
        max_length = 0
        for idx, n in enumerate(nums):
            if n == 0:
                count -= 1
            else:
                count += 1

            if count in seen:
                max_length = max(max_length, idx - seen[count])
            else:
                seen[count] = idx

        return max_length