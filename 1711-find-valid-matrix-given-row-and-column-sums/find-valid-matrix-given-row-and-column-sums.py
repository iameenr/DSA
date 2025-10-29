class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                x = min(rowSum[i], colSum[j])
                result[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x

        return result