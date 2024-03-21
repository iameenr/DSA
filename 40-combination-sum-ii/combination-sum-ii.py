class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []
        candidates.sort()
        
        def combination_sum(ind: int, target: int):
            if target == 0:
                result.append(list(comb))
                return
            
            for i in range(ind, len(candidates)):
                # Avoid duplicates
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue

                # Prune unnecessary branches
                if candidates[i] <= target:
                    comb.append(candidates[i])
                    combination_sum(i + 1, target - candidates[i])
                    comb.pop()
        
        combination_sum(0, target)
        return result