class Solution:
    def numDecodings(self, st: str) -> int:
        def f(idx) -> int:
            if idx == lens: 
                return 1

            if idx in memo:
                return memo[idx]

            split_onepart, split_twopart = 0, 0

            onepart = int(s[idx])
            if onepart >= 1 and onepart <= 9:
                split_onepart = f(idx+1)
                # split_onepart = f(s[1:])
            
            twopart = int("".join(s[idx:idx+2]))
            if twopart >= 10 and twopart <= 26:
                split_twopart = f(idx+2)
                # split_twopart = f(s[2:])
            
            memo[idx] = split_onepart + split_twopart
            return memo[idx]

        s = [c for c in st]
        lens = len(s)
        memo = {}
        return f(0)

