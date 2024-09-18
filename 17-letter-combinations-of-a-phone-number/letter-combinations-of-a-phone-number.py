class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine(index, combination):
            if index == lendigits:
                yield "".join(combination)
            else:
                for char in digits_to_letters[digits[index]]:
                    yield from combine(index+1, combination + [char])
            

        if digits == "": 
            return ""

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
        lendigits = len(digits)
        return [c for c in combine(0, [])]
        