from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character in the word
        char_frequency = Counter(word)

        total_pushes = 0
        # Sort frequencies in descending order
        for index, frequency in enumerate(sorted(char_frequency.values(), reverse=True)):
            # Each "row" of 8 characters requires one more push
            total_pushes += (index // 8 + 1) * frequency

        return total_pushes
