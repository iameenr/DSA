"""Better"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0

        longest_substring_len = 0
        start = 0
        window = set();   # {(char : index)}
        for end, char in enumerate(s):
            while char in window:
                window.remove(s[start])
                start += 1

            window.add(char)
            longest_substring_len = max(longest_substring_len, (end-start)+1)

        return longest_substring_len


