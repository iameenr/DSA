class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_index, path):
            result.append(list(path))
            
            for i in range(start_index, len(nums)):
                path.append(nums[i])     
                backtrack(i + 1, path)   
                path.pop()                

        result = []       
        backtrack(0, [])
        return result


        # def _get_subsets(index):
        #     if index >= lennums:
        #         yield []
        #         return 

        #     first = nums[index]
        #     for subset in _get_subsets(index + 1):
        #         yield subset
        #         yield [first] + subset

        # lennums = len(nums)
        # return list(_get_subsets(0))

        