class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(r, c):
            neighbors = []
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for i, j in directions:
                nr = r + i; nc = c + j
                if 0 <= nr < rowlen and 0 <= nc < collen and grid[nr][nc] == "1":
                    yield nr, nc
        
        def _dfs(r, c):
            grid[r][c] = "#"
            for nr, nc in get_neighbors(r, c):
                _dfs(nr, nc)

        rowlen = len(grid); collen = len(grid[0])
        islands = 0
        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c] == "1":
                    islands += 1
                    _dfs(r, c)

        return islands