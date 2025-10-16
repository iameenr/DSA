class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for k in range(n - 2, -1, -1):
            row, col = k, 0
            diagonal = []
            while row < n and col < n:
                diagonal.append(grid[row][col])
                row += 1
                col += 1

            diagonal.sort()
            row, col = k, 0
            while row < n and col < n:
                grid[row][col] = diagonal.pop()
                row += 1
                col += 1

        for k in range(n - 2, 0, -1):
            row, col = k, n - 1
            diagonal = []
            while row >= 0 and col >= 0:
                diagonal.append(grid[row][col])
                row -= 1
                col -= 1

            diagonal.sort()
            row, col = k, n - 1
            while row >= 0 and col >= 0:
                grid[row][col] = diagonal.pop()
                row -= 1
                col -= 1
                
        return grid
