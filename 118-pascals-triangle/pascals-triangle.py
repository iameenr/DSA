class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        1,5,10,10,5,1
        1,6,15,20,15,6,1
        1,7,21,35,35,21,7,1
        """
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result