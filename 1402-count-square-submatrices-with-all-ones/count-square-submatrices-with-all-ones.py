class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        temp = [[0] * n for _ in range(m)]
        result = 0

        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == 0:
                    continue
                if i == 0 or j == 0:
                    temp[i][j] = 1
                else:
                    temp[i][j] = min(temp[i - 1][j - 1], temp[i - 1][j], temp[i][j - 1]) + 1
                result += temp[i][j]

        return result