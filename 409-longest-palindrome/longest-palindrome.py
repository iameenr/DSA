class Solution:
    def longestPalindrome(self, s: str) -> int:
        string_set = set()
        for letter in s:
            if letter not in string_set:
                string_set.add(letter)
            else:
                string_set.remove(letter)
        if len(string_set) != 0:
            return len(s) - len(string_set) + 1
        else:
            return len(s)