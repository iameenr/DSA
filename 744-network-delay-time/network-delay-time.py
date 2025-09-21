import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj_list[u].append((v, w))

        distances = {vertex: float('infinity') for vertex in adj_list}
        distances[k] = 0
        # [(vertex, distances), ...]
        pq = [(k, 0)]

        while pq:
            vertex, distance = heapq.heappop(pq)
            if distance > distances[vertex]:
                continue

            for neighbor, weight in adj_list[vertex]:
                new_distance = distance + weight
                # old_distance = distances[neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (neighbor, new_distance))

        maxd = max(distances.values())
        return -1 if maxd == float('infinity') else maxd
