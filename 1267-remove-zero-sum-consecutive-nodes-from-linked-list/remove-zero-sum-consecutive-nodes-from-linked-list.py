"""
Q: 
subarray_sum = 0

prefix_sum(currpoint) - prefix_sum(prevpoint)  = 0
prefix_sum(currpoint) = prefix_sum(prevpoint)
"""

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        sum_dict = {0: dummy}
        curr = head
        
        while curr:
            prefix_sum += curr.val
            if prefix_sum in sum_dict:
                node = sum_dict[prefix_sum].next
                temp_sum = prefix_sum
                while node != curr:
                    # Remove all nodes between the previos point (exclusive) of the prefix_sum to the current_point (inclusive)
                    temp_sum += node.val
                    del sum_dict[temp_sum]
                    node = node.next
                
                # Linking the pp to cp
                sum_dict[prefix_sum].next = curr.next
            else:
                sum_dict[prefix_sum] = curr
            curr = curr.next
        
        return dummy.next