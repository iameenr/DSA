class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        prefix_sum_dict = {0 : 1} # prefix_sum : num of times it was seen
        times = 0
        
        for n in nums:
            prefix_sum += n

            target = prefix_sum - k
            if target in prefix_sum_dict:
                times = times + prefix_sum_dict[target]

            if prefix_sum not in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] = 0
            prefix_sum_dict[prefix_sum] += 1

        return times
