class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0

        longest_substring_so_far = 0
        window_start = 0
        window = set()  # set{ char, char2 }
        for end, char in enumerate(s):
            while char in window:
                window.remove(s[window_start])
                window_start += 1
            window.add(char)

            # current_window_length = (end - window_start) + 1
            longest_substring_so_far = max(longest_substring_so_far, (end - window_start) + 1)

        return longest_substring_so_far