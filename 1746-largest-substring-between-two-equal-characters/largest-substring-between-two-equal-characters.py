class Solution:
    def maxLengthBetweenEqualCharacters(self, string: str) -> int: 
        maxl = -1
        for s in range(len(string)):
            for e in range(len(string) - 1, s, -1):
                if string[s] == string[e]:
                    maxl = max(maxl, e - s - 1)
                    break  
        return maxl
