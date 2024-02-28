class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None): return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                """
                this point is prefix node length prior on the to the cycle start, 
                that is if you move prefix length then you'll be at the cycle start
                """
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow 

        return None
