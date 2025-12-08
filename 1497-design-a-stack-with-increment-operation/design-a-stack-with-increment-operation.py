class CustomStack:
    def __init__(self, max_size: int):
        self.stack = [0] * max_size
        self.increment_buffer = [0] * max_size
        self.size = 0

    def push(self, value: int) -> None:
        if self.size < len(self.stack):
            self.stack[self.size] = value
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        result = self.stack[self.size] + self.increment_buffer[self.size]
        if self.size > 0:
            self.increment_buffer[self.size - 1] += self.increment_buffer[self.size]
        self.increment_buffer[self.size] = 0
        return result

    def increment(self, count: int, value: int) -> None:
        index = min(count, self.size) - 1
        if index >= 0:
            self.increment_buffer[index] += value

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)