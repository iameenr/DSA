# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head is None): return False

        fast = head.next; slow=head
        while(fast != slow):
            if( fast is None 
                or fast.next is None 
                or fast.next.next is None):
                return False
            else:
                fast = fast.next.next
                slow = slow.next
        return True
