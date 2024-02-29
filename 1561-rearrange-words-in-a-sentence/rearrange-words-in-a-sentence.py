from heapq import heapify, heappush, heappop

class Solution:
    def arrangeWords(self, text: str) -> str:
        
        words = text.split(" ")
        heap = []  # (length, index)
        words[0] = words[0].lower()

        for i, w in enumerate(words):
            heappush(heap, (len(w), i))
  
        result = ""
        firstword = True
        while heap:
            _, i = heappop(heap)
            if firstword:
                result += words[i].capitalize() +" "
                firstword = False
            else:
                result += words[i] +" "

        return result[:-1]

