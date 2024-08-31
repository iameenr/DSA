class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _expand_from_center(l, r):
            while l >= 0 and r < lens and s[l] == s[r]:
                l = l - 1
                r = r + 1
            
            return l+1, r-1

        maxleft, maxright = 0, 0
        maxlen = -math.inf
        lens = len(s)
        for c in range(0, lens):
            # odd length
            # l, r = c, c
            currleft, currright = _expand_from_center(c, c)
            currlen = (currright-currleft)+1
            if currlen > maxlen:
                maxleft, maxright = currleft, currright
                maxlen = currlen

            # even length
            # l, r = c, c+1
            currleft, currright = _expand_from_center(c, c+1)
            currlen = (currright-currleft)+1
            if currlen > maxlen:
                maxleft, maxright = currleft, currright
                maxlen = currlen

        return s[maxleft:maxright+1]