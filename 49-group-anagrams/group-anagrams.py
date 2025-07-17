from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        # Map each lowercase letter to a distinct prime number.
        LETTER_TO_PRIME = {
            'a': 2,   'b': 3,   'c': 5,   'd': 7,   'e': 11,
            'f': 13,  'g': 17,  'h': 19,  'i': 23,  'j': 29,
            'k': 31,  'l': 37,  'm': 41,  'n': 43,  'o': 47,
            'p': 53,  'q': 59,  'r': 61,  's': 67,  't': 71,
            'u': 73,  'v': 79,  'w': 83,  'x': 89,  'y': 97,
            'z': 101
        }

        def prime_product(word):
            """Compute the product of the prime representations of the word's letters."""
            product = 1
            for char in word:
                product *= LETTER_TO_PRIME[char]
            return product

        """Group words that are anagrams."""
        groups = defaultdict(list)
        for word in words:
            key = prime_product(word)
            groups[key].append(word)
        
        return list(groups.values())


