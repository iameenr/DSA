class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(count):
            result = 0
            for i, n in count.items():
                if n > 0:
                    result += 1
                    count[i] -= 1
                    result += dfs(count)
                    count[i] += 1
            return result

        count = Counter(tiles)
        return dfs(count)