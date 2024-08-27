class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = 0
        all_psc = {0 : 1}
        res = 0
        for n in nums:
            ps += n

            key = ps - k

            if key in all_psc:
                res = res + all_psc[key]
            if ps not in all_psc:
                all_psc[ps] = 0

            all_psc[ps] += 1

        return res