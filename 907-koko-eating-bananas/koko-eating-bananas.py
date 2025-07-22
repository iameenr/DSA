import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_eating_speed = right

        while left <= right:
            mid_speed = (left + right) // 2
            
            eating_hours = 0
            for pile in piles:
                eating_hours += math.ceil(pile / mid_speed)

            if eating_hours <= h:
                min_eating_speed = mid_speed
                right = mid_speed - 1
            else:
                left = mid_speed + 1
                
        return min_eating_speed


#         # if h < numpiles: 
#         #     return -1 
#         # if h == numpiles: 
#         #     return max(piles) 
#         # if h > numpiles: 
#         #     solve