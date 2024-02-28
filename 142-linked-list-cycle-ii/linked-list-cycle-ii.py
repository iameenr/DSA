class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head

        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next

        return None  
