class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutations = list(range(1, m + 1))
        result = []

        for v in queries:
            j = permutations.index(v)
            result.append(j)
            permutations.pop(j)
            permutations.insert(0, v)
            
        return result