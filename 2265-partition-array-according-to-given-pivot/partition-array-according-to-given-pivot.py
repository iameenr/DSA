class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser_than_list, equal_to_list, greater_than_list = [], [], []

        for n in nums:
            if n < pivot:
                lesser_than_list.append(n)
            elif n == pivot:
                equal_to_list.append(n)
            else:
                greater_than_list.append(n)
                
        return lesser_than_list + equal_to_list + greater_than_list