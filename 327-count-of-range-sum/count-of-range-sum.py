class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        def sort_count(left: int, right: int) -> int:
            if right - left <= 1:   # zero or one element -> no pairs
                return 0
            mid = (left + right) // 2
            count = sort_count(left, mid) + sort_count(mid, right)

            # count cross-boundary pairs: i in [left, mid), j in [mid, right)
            j = k = mid
            for i in range(left, mid):
                # move j
                while j < right and prefix[j] - prefix[i] < lower:
                    j += 1
                # moving k
                while k < right and prefix[k] - prefix[i] <= upper:
                    k += 1
                # indices in [j, k) produce valid sums for this i
                count += (k - j)

            # standard merge to keep prefix[left:right] sorted
            merged = []
            p, q = left, mid
            while p < mid and q < right:
                if prefix[p] <= prefix[q]:
                    merged.append(prefix[p]); p += 1
                else:
                    merged.append(prefix[q]); q += 1
            # append remaining parts
            if p < mid:
                # merged
                merged.extend(prefix[p:mid])
            if q < right:
                merged.extend(prefix[q:right])
            # write back sortd slice
            prefix[left:right] = merged

            return count

        return sort_count(0, len(prefix))
