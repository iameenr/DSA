class Solution:
    def secondHighest(self, s: str) -> int:
        
        flargest, slargest = -1, -1
        for c in s:
            if c.isnumeric():
                n = int(c)
                if n > flargest:
                    slargest, flargest = flargest, n
                elif n != flargest and n > slargest:
                    slargest = n

        return slargest
