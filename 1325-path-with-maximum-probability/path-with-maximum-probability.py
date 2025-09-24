from heapq import heapify, heappush, heappop
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def get_adj_list():
            adj = defaultdict(list)  # { node: [(neighbor, w), ...]}
            for i, (u, v) in enumerate(edges):
                prob = succProb[i]
                adj[u].append((v, prob))
                adj[v].append((u, prob))

            return adj

        adj = get_adj_list()
        heap = [(-1.0, start)]
        prob = {v:0 for v in range(n)}
        prob[start] = 1.0

        while heap:
            p, node = heappop(heap)
            p = -p

            if node == end:
                return p
            
            if p < prob[node]:
                continue

            for neighbor, neighbor_probability in adj[node]:
                curr_neighbor_probability = p * neighbor_probability
                if curr_neighbor_probability > prob[neighbor]:
                    prob[neighbor] = curr_neighbor_probability
                    heappush(heap, (-curr_neighbor_probability, neighbor))

        if end in prob: 
            return prob[end]
        return 0.0 


