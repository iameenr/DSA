class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        n = len(nums)
        answer = [0] * n

        left_sum = 0
        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            answer[i] = abs(left_sum - right_sum)
            left_sum += nums[i]
            
        return answer