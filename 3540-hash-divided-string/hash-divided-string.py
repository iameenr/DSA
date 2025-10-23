class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        ALPHABETS_LENGTH = 26
        
        for i in range(0, len(s), k):
            t = 0
            for j in range(i, i + k):
                t += ord(s[j]) - ord("a")
            hash_char = t % ALPHABETS_LENGTH
            result.append(chr(ord("a") + hash_char))

        return "".join(result)