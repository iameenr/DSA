class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0

        longest_substring_yet = 0
        window_start = 0
        window = set();   # {(char : index)}
        for end, char in enumerate(s):
            while char in window:
                window.remove(s[window_start])
                window_start += 1
            window.add(char)

            longest_substring_yet = max(longest_substring_yet, (end-window_start)+1)

        return longest_substring_yet