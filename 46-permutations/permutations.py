class Solution:
    def __init__(self):
        self.lennums = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permutation(path, remaining):
            # Base case: If path length is equal to nums length
            if len(path) == self.lennums:
                yield path[:]
            else:
                for i in range(len(remaining)):
                    next_remaining = remaining[:i] + remaining[i+1:]
                    path.append(remaining[i])
                    yield from _permutation(path, next_remaining)
                    path.pop()

        self.lennums = len(nums)
        remaining = nums[:]
        result = [p for p in _permutation([], remaining)]
        return result