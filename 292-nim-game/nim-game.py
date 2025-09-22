class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        # 1 = w
        # 2 = w
        # 3 = w
        # 4 = l
        # 5 = force a w
        # 6 = force a w
        # 7 = force a w
        # 8 = l
        # 9 = force a w
        # ....
        """
        
        # will_loose = (n % 4 == 0)
        can_win = not (n % 4 == 0)
        return can_win
