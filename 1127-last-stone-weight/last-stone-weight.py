from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones

        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            first = abs(heapq.heappop(heap))
            second = abs(heapq.heappop(heap))
            if first != second:
                heapq.heappush(heap, -abs(first - second))
                
        # this compact return statement way is great ^_^
        return abs(heap[0]) if len(heap) else 0
                

        

        