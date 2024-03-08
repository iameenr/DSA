class Solution:
    def reorganizeString(self, S: str) -> str:
        n, counter = len(S), Counter(S)
        pq = [(-count, char) for char, count in counter.items()]
        heapq.heapify(pq)
        maxOccur = -1 * pq[0][0]
        if maxOccur > (n + 1) // 2:
            return ""
        string = [''] * n
        i = 0
        while pq:
            count, char = heapq.heappop(pq)
            count *= -1
            for j in range(count):
                string[i] = char
                i += 2
                if i >= n:
                    i = 1
        return "".join(string)