class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def _lcs(f, s, memo):
            if f < 0 or s < 0: return 0

            if memo[f][s] != -1:
                return memo[f][s]

            if text1[f] == text2[s]:
                lcs = 1 + _lcs(f-1, s-1, memo)
            else:
                lcs = max(_lcs(f-1, s, memo), _lcs(f, s-1, memo))

            memo[f][s] = lcs
            return lcs

        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return _lcs(len(text1)-1, len(text2)-1, memo)