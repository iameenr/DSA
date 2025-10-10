class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                rows[i] += v
                cols[j] += v
        difference = [[0] * n for _ in range(m)]

        for i, row in enumerate(rows):
            for j, col in enumerate(cols):
                difference[i][j] = row + col - (n - row) - (m - col)

        return difference