class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_distance = math.inf
        closest_number = nums[0]

        for n in nums:
            distance = abs(n)
            if distance < closest_distance or \
               (distance == closest_distance and n > closest_number):
                closest_distance = distance
                closest_number = n
                
        return closest_number