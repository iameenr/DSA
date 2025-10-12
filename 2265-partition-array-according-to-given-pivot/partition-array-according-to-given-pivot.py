class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt, eq, gt = [], [], []

        for n in nums:
            if n < pivot:
                lt.append(n)
            elif n == pivot:
                eq.append(n)
            else:
                gt.append(n)
        return lt + eq + gt