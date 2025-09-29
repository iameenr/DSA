class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lenofll = 0
        node = head

        while node:
            lenofll += 1
            node = node.next

        ridx = lenofll - n
        node = dummy
        for _ in range(ridx):
            node = node.next
            
        node.next = node.next.next
        return dummy.next
