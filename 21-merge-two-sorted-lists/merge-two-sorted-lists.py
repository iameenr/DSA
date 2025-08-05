
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # Traverse both lists as long as neither is exhausted.
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Move the tail pointer to the newly added node.
            tail = tail.next
        
        tail.next = list1 or list2
            
        return dummy.next