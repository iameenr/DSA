class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        set1 = set(nums1)
        for n in nums2:
            if n in set1:
                set1.remove(n)
                intersection.append(n)

        return intersection
