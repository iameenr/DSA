class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_score = [0] * (n + 1)  

        for a, b in trust:
            # Decrement a because they trust someone
            trust_score[a] -= 1
            # Increment b because someone trusts them
            trust_score[b] += 1
        
        # Check for the town judge based on trust score
        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i
        
        # If no judge found, return -1
        return -1

