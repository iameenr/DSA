class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        res = []

        while num != 0:
            # remainder = num % 7
            res.append(str(num % 7))
            num //= 7

        if negative:
            res.append('-')

        return "".join(res[::-1])

