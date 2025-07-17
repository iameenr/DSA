class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]

            # Check mapping from s to t
            if char_s not in map_s:
                map_s[char_s] = char_t
            elif map_s[char_s] != char_t:
                return False  # Existing mapping for char_s is different

            # Check mapping from t to s
            if char_t not in map_t:
                map_t[char_t] = char_s
            elif map_t[char_t] != char_s:
                return False  # Existing mapping for char_t is different
        
        return True