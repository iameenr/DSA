class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = max_window_length = 0
        window = dict()

        for end, c in enumerate(s):

            if window.get(c, -1) >= start:
                start = window[c] + 1

            max_window_length = max(max_window_length, end - start + 1)
            window[c] = end

        return max_window_length
        