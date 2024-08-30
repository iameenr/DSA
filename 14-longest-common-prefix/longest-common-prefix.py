class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        lcs = ""
        v = sorted(v)
        first = v[0] 
        last  = v[-1]
        
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return lcs
            lcs += first[i]
        return lcs 