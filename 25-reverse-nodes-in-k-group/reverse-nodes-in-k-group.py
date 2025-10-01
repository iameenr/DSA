class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, end):
            prev = None
            current = head
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        length = getLength(head)

        dummy_head = ListNode(0)
        dummy_head.next = head
        prev_group_end = dummy_head
        
        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next
            next_group_start = group_end.next
            # reverse the group
            prev_group_end.next = reverseLinkedList(group_start, next_group_start)
            group_start.next = next_group_start
            prev_group_end = group_start
            length -= k
            
        return dummy_head.next
