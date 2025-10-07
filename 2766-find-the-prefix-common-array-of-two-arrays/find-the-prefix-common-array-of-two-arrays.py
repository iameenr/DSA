class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        restult = []

        counter_1 = Counter()
        counter_2 = Counter()
        for a, b in zip(A, B):
            counter_1[a] += 1
            counter_2[b] += 1
            t = sum(min(v, counter_2[x]) for x, v in counter_1.items())
            restult.append(t)
            
        return restult