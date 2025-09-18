class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_array, right_array):
            merged = []
            
            left_idx = right_idx = 0
            # for left_idx in range(0, len(left_array)):
            while left_idx < len(left_array) and \
                  right_idx < len(right_array):
                if left_array[left_idx] <= right_array[right_idx]:
                    merged.append(left_array[left_idx])
                    left_idx += 1
                else:
                    merged.append(right_array[right_idx])
                    right_idx += 1
            
            # append rest
            merged.extend(left_array[left_idx:])
            merged.extend(right_array[right_idx:])

            return merged
                
        def merge_sort(array):
            lenarray = len(array)
            if lenarray <= 1:
                return array # a single element is always sorted

            mid = (0 + lenarray) // 2
            left = array[:mid]
            right = array[mid:]
            
            # sortedarray = merge(
            #     merge_sort(left), merge_sort(right)
            # )

            return merge(
                merge_sort(left), merge_sort(right)
            )

        
        return merge_sort(nums)

