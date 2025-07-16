class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]
            
            if curr == target:
                return [left + 1, right + 1]
            elif curr > target: 
                # current sum is greater, so we must reduce it
                right -= 1
            else: 
                # curr < target, current sum is lesser, so we must increase it
                left += 1

        # Should be uncreacheable 
        return []
            

