class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_stops = len(gas) - 1
        total_gas  = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost: # not possible
            return -1

        total_net_cost = 0
        start_idx = 0
        for i in range(total_stops+1):
            net_cost = gas[i] - cost[i]
            total_net_cost += net_cost

            if total_net_cost < 0: # reset
                total_net_cost = 0
                start_idx = i+1

        return start_idx
        