class Solution:
    def singleNumber(self, nums):
        count_map = defaultdict(int)
        
        for n in nums:
            count_map[n] += 1

        for n, freq in count_map.items():
            if freq == 1:
                return n
        
        return -1