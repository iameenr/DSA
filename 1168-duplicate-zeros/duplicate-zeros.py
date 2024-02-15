class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes_count = 0  
        length_ = len(arr) - 1

        # Find the number of possible duplicates and the rightmost index 
        for left in range(length_ + 1):
            if left > length_ - zeroes_count:
                break
            if arr[left] == 0:
                if left == length_ - zeroes_count:  # Edge case for a last zero
                    arr[length_] = 0  
                    length_ -= 1
                    break
                zeroes_count += 1

        # Start from the end and shift elements for duplication
        last = length_ - zeroes_count  
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + zeroes_count] = 0
                zeroes_count -= 1
                arr[i + zeroes_count] = 0
            else:
                arr[i + zeroes_count] = arr[i]
