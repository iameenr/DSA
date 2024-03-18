class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        
        START, END = 0, 1
        arrows = 1
        end = points[0][1]
        for balloon in points[1:]:
            if balloon[START] > end: 
                arrows += 1  
                end = balloon[END] 
            else:
                end = min(end, balloon[1])
        
        return arrows