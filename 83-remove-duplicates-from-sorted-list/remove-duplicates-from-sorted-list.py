class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current_node = head

        while current_node and current_node.next:
            if current_node.val == current_node.next.val:  # Duplicate found
                current_node.next = current_node.next.next 
            else:
                current_node = current_node.next  

        return head
