class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        
        # prefix_xor[i] = XOR of arr[0...so_on..i-1]
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        total_triplets = 0

        # Check all possible (i, j,k)
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    left = prefix_xor[j] ^ prefix_xor[i]
                    right = prefix_xor[k + 1] ^ prefix_xor[j]
                    if left == right:
                        total_triplets += 1

        return total_triplets
