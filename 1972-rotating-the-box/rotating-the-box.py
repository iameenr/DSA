from collections import deque

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        num_rows, num_cols = len(box), len(box[0])

        # Initialize rotated box with None placeholders
        rotated_box = [[None] * num_rows for _ in range(num_cols)]

        # Rotate the box 90 degrees clockwise
        for row_index in range(num_rows):
            for col_index in range(num_cols):
                rotated_box[col_index][num_rows - row_index - 1] = box[row_index][col_index]

        # Apply gravity to stones ('#') in the rotated box
        for col_index in range(num_rows):
            empty_positions = deque()
            for row_index in range(num_cols - 1, -1, -1):
                if rotated_box[row_index][col_index] == '*':
                    empty_positions.clear()  # obstacle resets available positions
                elif rotated_box[row_index][col_index] == '.':
                    empty_positions.append(row_index)  # mark empty space
                elif empty_positions:
                    # Move stone down to the nearest empty position
                    rotated_box[empty_positions.popleft()][col_index] = '#'
                    rotated_box[row_index][col_index] = '.'
                    empty_positions.append(row_index)

        return rotated_box
