class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        roman_numeral = []
        for value in roman_map:  # Iterating through a dictionary in Python 3.7+ preserves insertion order
            while num >= value:
                roman_numeral.append(roman_map[value])
                num -= value
        
        return "".join(roman_numeral)