class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        def get_last_occurence(s):
            last_occurence = {}  # Store the last occurrence of each character
            for i, c in enumerate(s):
                last_occurence[c] = i
            return last_occurence

        last_occurence = get_last_occurence(s)
        start, end = 0, last_occurence[s[0]]
        lens = len(s)
        partitions = []  

        while start < lens:
            i = start
            end = last_occurence[s[start]]  
    
            while i <= end:
                end = max(end, last_occurence[s[i]])  # Extend the partition 
                i += 1
            partitions.append((end - start) + 1)  
            start = end + 1

        return partitions
