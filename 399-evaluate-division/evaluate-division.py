from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def get_adjlist(edges, weights):
            adjacency_list = defaultdict(list)
            for idx, (u, v) in enumerate(edges):
                adjacency_list[u].append((v, weights[idx]))
                adjacency_list[v].append((u, 1 / weights[idx]))
            return adjacency_list

        def find_path_dfs(curr, target, product, visited):
            if curr == target:
                return product
            visited.add(curr)
            for nei, weight in adjacency_list[curr]:
                if nei not in visited:
                    result = find_path_dfs(nei, target, (product * weight), visited)
                    if result != -1.0: 
                        return result

            return -1.0 # Target not found in the path of the DFS


        adjacency_list = get_adjlist(equations, values)
        results = []

        for start, end in queries:
            if start not in adjacency_list or end not in adjacency_list:
                results.append(-1.0)
            elif start == end:
                results.append(1.0)
            else:
                visited = set()
                result = find_path_dfs(start, end, 1.0, visited)
                results.append(result)

        return results
