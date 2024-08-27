class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_dict = {0 : 1}

        result = 0
        for n in nums:
            prefix_sum = prefix_sum + n
            want = prefix_sum - k
            
            if want in prefix_sum_dict:
                result += prefix_sum_dict[want]

            if prefix_sum not in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] = 0
                
            prefix_sum_dict[prefix_sum] += 1

        return result