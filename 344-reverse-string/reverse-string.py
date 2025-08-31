class Solution:
    def reverseString(self, s: List[str]) -> None:
        forward, backward = 0, len(s)-1
        while forward < backward:
            s[forward], s[backward] = s[backward], s[forward]
            forward += 1
            backward -= 1