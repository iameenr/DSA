import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.value_index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.value_index_map:
            return False

        self.values.append(val)
        self.value_index_map[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_index_map:
            return False

        # removal_index = self.value_index_map[val]
        # last_value = self.values[-1]
        # self.values[removal_index] = last_value
        # self.value_index_map[last_value] = removal_index
        #
        # self.values.pop()
        # del self.value_index_map[val]

        removal_index = self.value_index_map[val]
        del self.value_index_map[val]

        if removal_index != (len(self.values) - 1):
            last_value = self.values[-1] # replace with last value
            self.values[removal_index] = last_value
            self.value_index_map[last_value] = removal_index

        self.values.pop()
        return True


    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()