class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge_intervals(intervals):
            if not intervals:
                return []

            START, END = 0, 1
            left = 0  # Pointer to the last non-merged interval
            for right in range(1, len(intervals)):
                # If the current interval can be merged with the last non-merged interval
                if intervals[left][END] >= intervals[right][START]:
                    intervals[left][END] = max(intervals[left][END], intervals[right][END])
                else:
                    left += 1
                    intervals[left] = intervals[right]

            return intervals[:left+1]
        
  

        new_interval_start = newInterval[0]
        index = len(intervals)
        # insert the new interval into its proper position
        for i, interval in enumerate(intervals):
            if new_interval_start <= interval[0]:
                index = i
                break
 
        # insert new interval in index
        intervals.insert(index, newInterval)
        return merge_intervals(intervals)
            