class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0

        frequency = collections.Counter(s)

        for i, char in enumerate(s):
            # If the character's frequency is less than k, split the string
            if frequency[char] < k:
                left_part = self.longestSubstring(s[:i], k)
                right_part = self.longestSubstring(s[i+1:], k)
                return max(left_part, right_part)

        # If no character with frequency less than k was found, 
        # return the length of the string
        return len(s)
