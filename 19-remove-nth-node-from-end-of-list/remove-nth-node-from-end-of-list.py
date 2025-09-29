class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """one pass solution"""
        dummy = ListNode(0, head)
        first = sec = dummy

        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            sec = sec.next
        
        sec.next = sec.next.next

        return dummy.next


"""two pass soln"""
# dummy = ListNode(0, head)
# lenofll = 0
# node = head

# while node:
#     lenofll += 1
#     node = node.next

# ridx = lenofll - n
# node = dummy
# for _ in range(ridx):
#     node = node.next

# node.next = node.next.next
# return dummy.next
