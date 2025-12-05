class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_capacity = capacity
        for index, water_needed in enumerate(plants):
            if current_capacity >= water_needed:
                current_capacity -= water_needed
                steps += 1
            else:
                current_capacity = capacity - water_needed
                steps += index * 2 + 1
        return steps
