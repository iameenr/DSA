from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        """the product of 2 or more prime numbers is always unique
            so this helps us uniquely identify words formed from same set of letters."""

        LETTER_TO_PRIME = {
            'a': 2,   'b': 3,   'c': 5,   'd': 7,   'e': 11,
            'f': 13,  'g': 17,  'h': 19,  'i': 23,  'j': 29,
            'k': 31,  'l': 37,  'm': 41,  'n': 43,  'o': 47,
            'p': 53,  'q': 59,  'r': 61,  's': 67,  't': 71,
            'u': 73,  'v': 79,  'w': 83,  'x': 89,  'y': 97,
            'z': 101
        }

        def get_prime_product(word):
            prime_product = 1
            for c in word:
                prime_product *= LETTER_TO_PRIME[c]

            return prime_product

        
        result = defaultdict(list) # {1562: [eat, tea, ate]}
        for word in words:
            prime_product = get_prime_product(word)
            result[prime_product].append(word)

        return [anagram for anagram in result.values()]


