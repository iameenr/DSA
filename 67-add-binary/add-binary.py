

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(self._to_base_two(a) + self._to_base_two(b))[2:]

    def _to_base_two(self, s):
        base_two = 0
        for digit in s:
            base_two = 2*base_two + int(digit)

        return base_two