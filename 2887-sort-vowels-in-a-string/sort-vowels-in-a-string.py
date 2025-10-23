class Solution:
    def sortVowels(self, s: str) -> str:
        # vowels = []
        # vowel_indices = []
        # sort vowels
        # replace sorted vowels in vowle_indices

        vowelset = {
            'A', 'E', 'I', 'O', 'U',
            'a', 'e', 'i', 'o', 'u'
        }

        vowels = []
        vowel_indices = []
        for i, c in enumerate(s):
            if c in vowelset:
                vowels.append(c)
                vowel_indices.append(i)

        vowels.sort()

        t_list = list(s)
        i = 0
        for index in vowel_indices:
            t_list[index] = vowels[i]
            i += 1
        
        return "".join(t_list)


