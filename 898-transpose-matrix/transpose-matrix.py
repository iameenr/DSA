class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rowllen, collen = len(matrix), len(matrix[0])
        result_matrix = [[0] * rowllen for _ in range(collen)]

        for r in range(rowllen):
            for c in range(collen):
                result_matrix[c][r] = matrix[r][c]
        
        return result_matrix