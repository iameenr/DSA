class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        def get_first_last_occurence(s):
            first_last_dict = {} # c : [foc, loc] | a : [0, 9]
            LOC = 1
            seen = set()
            for i, c in enumerate(s):
                if c in seen:
                    # next occurence
                    first_last_dict[c][LOC] = i
                else:
                    # first_last_dict[c][FOC], first_last_dict[c][LOC] = i, i
                    first_last_dict[c] = [i, i]
                    seen.add(c)

            return first_last_dict

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

        first_last_dict = get_first_last_occurence(s)

        intervals = []
        for k, v in first_last_dict.items():
            intervals.append(v)

        merged_intervals = merge_overlapping_intervals(intervals)

        # take sum and return 
        partitions = []
        for s, e in merged_intervals:
            partitions.append((e-s)+1)

        return partitions
