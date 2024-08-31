class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _expand_from_center(l, r):
            while l >= 0 and r < lens and s[l] == s[r]:
                l = l - 1
                r = r + 1
            
            return l+1, r-1

        least_left, max_right = 0, 0
        maxlen = -math.inf
        lens = len(s)
        for center in range(0, lens):
            # odd length
            # l, r = center, center
            li, ri = _expand_from_center(center, center)
            if (ri - li) + 1 > (max_right - least_left) + 1:
                least_left, max_right = li, ri

            # even length
            # l, r = center, center+1
            li, ri = _expand_from_center(center, center+1)
            if (ri - li) + 1 > (max_right - least_left) + 1:
                least_left, max_right = li, ri

        return s[least_left:max_right+1]