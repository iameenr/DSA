class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        res = []
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1

        while row_begin <= row_end and col_begin <= col_end:
            # Traverse Right
            for j in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][j])
            row_begin += 1

            # Traverse Down
            for j in range(row_begin, row_end + 1):
                res.append(matrix[j][col_end])
            col_end -= 1

            if row_begin <= row_end:
                # Traverse Left
                for j in range(col_end, col_begin - 1, -1):
                    res.append(matrix[row_end][j])
                row_end -= 1

            if col_begin <= col_end:
                # Traverse Up
                for j in range(row_end, row_begin - 1, -1):
                    res.append(matrix[j][col_begin])
                col_begin += 1

        return res
        