class Solution(object):
    def letterCombinations(self, digits):
        def backtrack(c, i):
            if i == len(digits):
                yield c
            else:
                for l in digits_to_letters[digits[i]]:
                    yield from backtrack(c + l, i+1)


        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
         }
        
        if digits == "": return ""            
        return [combination for combination in backtrack("", 0)]