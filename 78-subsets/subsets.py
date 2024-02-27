class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _subsets(ls):
            if not ls:
                yield []
            else:
                # first = ls[0]
                # rest  = ls[1:]
                for subset in _subsets(ls[1:]):
                    yield subset
                    yield [ls[0]] + subset  

        return [subset for subset in _subsets(nums)]


