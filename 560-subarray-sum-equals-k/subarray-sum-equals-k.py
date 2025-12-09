from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_sum(curr) - prefix_sum(prev) = k
        # prefix_sum(curr) - k = prefix_sum(prev) 

        prefix_sum_dict = defaultdict(int) # {sum : number of times we've seen this sum}
        prefix_sum_dict[0] = 1
        prefix_sum = 0

        result = 0
        for n in nums:
            prefix_sum += n
            if(prefix_sum - k) in prefix_sum_dict:
                result += prefix_sum_dict[(prefix_sum - k)]
            prefix_sum_dict[prefix_sum] += 1
        
        return result

            

