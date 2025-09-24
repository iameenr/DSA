class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman_ford
        def get_graph_adj_list(array):
            graph_adj_list = defaultdict(dict) # {node: [{neigh: w}, ...]}
            for u, v, w in flights:
                graph_adj_list[u][v] = w

            return graph_adj_list

        graph_adj_list = get_graph_adj_list(flights)
        prices = {node: (float('infinity'), float('infinity')) for node in range(n)} # distance;  {city : (lpy, stops)}
        prices[src] = (0, 0)
        # print(graph_adj_list)

        for _ in range(k+1): # relax edges k + 1 times
            new_prices = prices.copy()
            for node in graph_adj_list:
                cptn, stops = prices[node]
                if cptn == float('infinity'):
                    continue
                for neigh, price in graph_adj_list[node].items():
                    oldprice, oldstops = new_prices[neigh]
                    relaxed = cptn + price
                    # print(relaxed < oldprice, ((stops+1) <= k))
                    if relaxed < oldprice:
                        new_prices[neigh] = (relaxed, stops+1)
            prices = new_prices


        cheapest_price = prices[dst][0]
        if cheapest_price == float('infinity'):
            cheapest_price = -1
        return cheapest_price