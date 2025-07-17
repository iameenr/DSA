class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        character_map = {}     # e : a, g : d
        mapped_characters = {} # a : e, d : g
        for index, char_s in enumerate(s):
            if char_s not in character_map:
                char_t = t[index]
                if char_t not in mapped_characters:
                    character_map[char_s] = char_t
                    mapped_characters[char_t] = char_s
                else:
                    if mapped_characters[char_t] != char_s:
                        return False
            else: # index have seen this character
                if character_map[char_s] != t[index]:
                    return False

        return True         
