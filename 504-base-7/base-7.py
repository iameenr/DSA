class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        IS_NEGATIVE = num < 0
        num = abs(num)
        res = []

        while num != 0:
            # remainder = num % 7
            res.append(str(num % 7))
            num //= 7

        if IS_NEGATIVE:
            res.append('-')

        # reverse a list ::-1
        return "".join(res[::-1])