class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: 
            return 0

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def is_valid_neighbor(r, c, nr, nc):
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] > matrix[r][c]:
                return True
            return False

        def dfs(r, c, matrix, memo):
            if (r, c) in memo: 
                return memo[(r, c)]
            
            # Initialize the length of the current path as 1 (current cell)
            max_len = 1
            # Explore the neighboring cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check if the neighboring cell is within matrix bounds
                # ..and if its value is greater than the current cell's value
                if is_valid_neighbor(r, c, nr, nc):
                    len_path = 1 + dfs(nr, nc, matrix, memo)
                    max_len = max(max_len, len_path)
            
            memo[(r, c)] = max_len
            return max_len
        
        memo = {}
        max_result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_result = max(max_result, dfs(i, j, matrix, memo))
        
        return max_result