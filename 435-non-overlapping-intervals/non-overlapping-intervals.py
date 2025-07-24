class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by their end points
        intervals.sort(key=lambda x: x[1])

        removals = 0
        last_end = intervals[0][1]

        # Iterate from the second interval
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            
            # If the current interval overlaps with the last one we kept,
            # we must remove it.
            if current_start < last_end:
                removals += 1
            # Otherwise, we keep the current interval and update the end point.
            else:
                last_end = intervals[i][1]

        return removals