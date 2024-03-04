class Solution:
    def maxLengthBetweenEqualCharacters(self, string: str) -> int: 
        start_index = {}
        max_length = -1

        for end, char in enumerate(string):
            if char not in start_index:
                start_index[char] = end
            max_length = max(max_length, ((end - start_index[char] - 1)))

        return max_length
