class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        res = []

        while num != 0:
            rem = num % 7
            res.append(str(rem))
            num = num // 7

        if negative:
            res.append('-')

        return "".join(reversed(res))
