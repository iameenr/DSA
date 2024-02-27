class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _subsets(index):
            if index == numslen:
                yield []
            else:
                # first = [nums[index]]
                # rest = index + 1
                for subset in _subsets(index + 1):
                    yield subset
                    yield [nums[index]] + subset
        
        numslen = len(nums)
        return [subset for subset in _subsets(0)]


