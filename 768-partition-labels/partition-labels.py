class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        def get_last_occurence(s):
            last_occurence = {} # c : loc like a : 9
            for i, c in enumerate(s):
                last_occurence[c] = i

            return last_occurence

        def merge_overlapping_intervals(intervals):
            # merge_overlapping intervals
            intervals.sort(key=lambda x:x[0])


            lenintervals = len(intervals)   

            merged_intervals = [intervals[0]]
            for i in range(1, lenintervals):
                cs, ce = intervals[i]
                le = merged_intervals[-1][1]

                if le > cs: #overlap
                    merged_intervals[-1][1] = max(le, ce)
                else:
                    merged_intervals.append([cs, ce])

            return merged_intervals

        last_occurence = get_last_occurence(s)

        intervals = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
                intervals.append([i, last_occurence[c]])


        merged_intervals = merge_overlapping_intervals(intervals)

        # take sum and return 
        partitions = []
        for s, e in merged_intervals:
            partitions.append((e-s)+1)

        return partitions
