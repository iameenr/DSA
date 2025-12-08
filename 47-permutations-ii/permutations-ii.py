class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]
        if not nums:
            return permutations

        for number in nums:
            updated_permutations = []
            for permutation in permutations:
                for index in range(len(permutation) + 1):
                    candidate = permutation[:index] + [number] + permutation[index:]
                    if candidate not in updated_permutations:
                        updated_permutations.append(candidate)
            permutations = updated_permutations
            
        return permutations
