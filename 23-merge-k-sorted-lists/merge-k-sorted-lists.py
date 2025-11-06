# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop
import itertools

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = ListNode(0)
        merged_dummy = merged
        tie_break_counter = itertools.count()

        heap = [] 
        for list_head in lists:
            if list_head:
                heappush(heap, (list_head.val, next(tie_break_counter), list_head))
        
        while heap:
            _, _, current_min_node = heappop(heap)
            merged.next = current_min_node
            merged = merged.next

            if current_min_node.next:
                heappush(heap, (current_min_node.next.val, next(tie_break_counter), current_min_node.next))

        return merged_dummy.next
            
