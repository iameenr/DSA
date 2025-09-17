class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        n = len(nums)
        answer = [0] * n

        prefix_sum = 0
        for i in range(n):
            suffix_sum = total_sum - prefix_sum - nums[i]
            answer[i] = abs(prefix_sum - suffix_sum)
            prefix_sum += nums[i]
            
        return answer