class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) == 0): 
            return True
            
        sp=0; tp=0
        while(tp<len(t)):
            if(s[sp]==t[tp]):
                sp+=1
            tp+=1
            if(sp==len(s)):
                return True

        return False

        