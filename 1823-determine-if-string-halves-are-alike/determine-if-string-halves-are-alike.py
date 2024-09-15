class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()  
        lens = len(s)  
        
        vowels = ['a', 'e', 'i', 'o', 'u']  
        first_half_count = 0
        second_half_count = 0
        
        # Count vowels in the first half of the string
        for c in s[0:(lens // 2)]:
            if c in vowels:
                first_half_count += 1
        
        # Count vowels in the second half of the string
        for c in s[(lens // 2):]:
            if c in vowels:
                second_half_count += 1
        
        return first_half_count == second_half_count
