from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ps(curr) - ps(prev) = k
        # ps(curr) - k = ps(prev) 

        psd = defaultdict(int) # {sum : number of times we've seen this sum}
        psd[0] = 1
        ps = 0

        result = 0
        for n in nums:
            ps += n
            if(ps - k) in psd:
                result += psd[(ps - k)]
            psd[ps] += 1
        
        return result

            

