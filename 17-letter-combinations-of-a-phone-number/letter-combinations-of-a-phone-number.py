class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
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

        def combine(index, combination):
            if index == end:
                combinations.append("".join(combination))
                return

            # digit = digits[index]
            for c in digits_to_letters[digits[index]]:
                combine(index+1, combination + [c])
            

        if digits == "": 
            return []

        end = len(digits)
        combinations = []
        combine(0, [])
        return combinations