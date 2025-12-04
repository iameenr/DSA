from collections import Counter

class Solution:
    def findSmallestSetOfVertices(self, num_vertices: int, edges: List[List[int]]) -> List[int]:
        # Count how many times each vertx appears as a target (inc edge)
        incoming_edge_count = Counter(target for _, target in edges)

        # Vertices with zero incoming edges are the smallest set of starting points
        source_vertices = [
            vertex for vertex in range(num_vertices) if incoming_edge_count[vertex] == 0
        ]

        return source_vertices