class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(index, path):
            if index == (n-1):
                paths.append(path)
            for nei in graph[index]:
                dfs(nei, path + [nei])    

        n = len(graph)
        paths = []
        dfs(0, [0])
        return paths