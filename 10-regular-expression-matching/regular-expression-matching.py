class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        match_table = [[False] * (n + 1) for _ in range(m + 1)]
        match_table[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    match_table[i][j] = match_table[i][j - 2]
                    if i > 0 and (p[j - 2] == "." or s[i - 1] == p[j - 2]):
                        match_table[i][j] |= match_table[i - 1][j]
                elif i > 0 and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                    match_table[i][j] = match_table[i - 1][j - 1]

        return match_table[m][n]