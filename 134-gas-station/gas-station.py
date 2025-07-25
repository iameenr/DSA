class Solution:
  def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
    total_tank = 0
    current_tank = 0
    start_station = 0
    
    for i in range(len(gas)):
      # Update total and current tank balances with the net gain/loss at station i.
      net_cost = gas[i] - cost[i]
      total_tank += net_cost
      current_tank += net_cost
      
      # If current_tank is negative, it means we can't reach station i+1
      # from the current start_station.
      if current_tank < 0:
        # The new potential starting point is the next station.
        start_station = i + 1
        # Reset the tank for the new journey segment.
        current_tank = 0
        
    # If total_tank is non-negative, a solution exists.
    # The start_station found is the correct one.
    # Otherwise, it's impossible to complete the circuit.
    if total_tank >= 0:
        return start_station
    else:
        return -1