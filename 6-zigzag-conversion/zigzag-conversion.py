class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        # Use a list of lists of characters for each row
        # This avoids repeated string concatenations which can be slow
        rows = [[] for _ in range(numRows)]

        current_row = 0
        direction = 1 # 1 for going down, -1 for going up

        for char in s:
            rows[current_row].append(char)

            # Change direction if at the top or bottom row
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        # Join characters in each row and then join the rows
        # The first join creates strings from lists of chars (e.g., ['P', 'A'] -> "PA")
        # The second join concatenates these row strings (e.g., "PA" + "PL" -> "PAPL")
        return "".join(["".join(row) for row in rows])