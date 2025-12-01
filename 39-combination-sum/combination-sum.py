class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combination(i, target, seq):
            if target == 0:
                yield seq
            else:
                n = candidates[i]
                if n <= target:
                    # use this index again
                    yield from combination(i, target - n, seq + [n])

                    # skip to next index
                    if i+1 < len(candidates):
                        yield from combination(i+1, target, seq)
            

        return [c for c in combination(0, target, [])]