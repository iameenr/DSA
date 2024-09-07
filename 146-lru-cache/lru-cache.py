class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node):
        self._remove_node(node)
        self._add_node(node)

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                oldest_node = self.head.next
                self._remove_node(oldest_node)
                del self.cache[oldest_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_end(node)
            return node.value
        return -1