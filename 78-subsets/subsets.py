class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lennums = len(nums)
        def _get_subsets(index):
            if index >= lennums:
                yield []
                return 

            first = nums[index]
            # rest = nums[index:]
            for subset in _get_subsets(index + 1):
                yield subset
                yield [first] + subset

        return list(_get_subsets(0))

        