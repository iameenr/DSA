class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """merge intervals"""
        
        fld = {} # c : [foc, loc] | a : [0, 9]
        LOC = 1
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                # next occurence
                fld[c][LOC] = i
            else:
                # fld[c][FOC], fld[c][LOC] = i, i
                fld[c] = [i, i]
                seen.add(c)


        intlist = []
        for k, v in fld.items():
            intlist.append(v)

        # merge_overlapping intervals
        intlist.sort(key=lambda x:x[0])


        lenintervals = len(intlist)   

        result = [intlist[0]]
        for i in range(1, lenintervals):
            cs, ce = intlist[i]
            le = result[-1][1]

            if le > cs: #overlap
                result[-1][1] = max(le, ce)
            else:
                result.append([cs, ce])

        # take sum and return 
        partitions = []
        for s, e in result:
            partitions.append((e-s)+1)

        return partitions
