from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_len = 0
        last_occurrence = defaultdict(int)
        
        # slide a window until you keep having two distinct values inside the window
        for end in range(len(fruits)):
            curr_fruit = fruits[end]
            
            if curr_fruit not in last_occurrence and len(last_occurrence) == 2:
            # trim the window from start until we have only one fruit left,
            # ..so we can accomodate this new fruit
                leftmost = min(last_occurrence.values())
                del last_occurrence[fruits[leftmost]]
                start = leftmost + 1

            max_len = max(max_len, end - start + 1)
            last_occurrence[curr_fruit] = end
            
        return max_len