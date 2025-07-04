class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        reversed_x = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reversed_x = (reversed_x*10) + digit
            temp = temp //10

        return reversed_x == x 