import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.last_index = -1
        self.value_index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.value_index_map:
            return False

        self.values.append(val)
        self.last_index += 1
        self.value_index_map[val] = self.last_index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_index_map:
            return False

        removal_index = self.value_index_map[val]
        del self.value_index_map[val]

        if removal_index != self.last_index:
            last_value = self.values[self.last_index] # replace with last value
            self.values[removal_index] = last_value
            self.value_index_map[last_value] = removal_index
        
        self.values.pop()
        self.last_index -= 1
        return True


    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()