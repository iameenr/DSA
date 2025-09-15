class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        for current_idx in range(1, len(intervals)):
            current_start_time, current_end_time = intervals[current_idx]
            previous_end_time = result[-1][1]
            
            # If current interval's start time is less than or equal to 
            # the last interval's end time in the result list, they overlap
            if current_start_time <= previous_end_time:
                # Merge the intervals by updating the end time of the last interval in the result list
                result[-1][1] = max(previous_end_time, current_end_time)
            else:
                # Otherwise, add the current interval to the result list
                # result.append(intervals[current_idx])
                result.append([current_start_time, current_end_time])
        
        return result
