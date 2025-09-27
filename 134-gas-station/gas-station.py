class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ts = len(gas) - 1
        tg = tc = 0
        for i in range(ts+1):
            tg += gas[i]
            tc += cost[i]
        if tg < tc: # not possible
            return -1

        tnc = 0
        start_idx = 0
        for i in range(ts+1):
            nc = gas[i] - cost[i]
            tnc += nc

            if tnc < 0:
                # reset
                tnc = 0
                start_idx = i+1

        return start_idx
        