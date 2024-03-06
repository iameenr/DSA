# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, node: Optional[ListNode]) -> Optional[ListNode]:
        resulthead = ListNode()
        resultnode = resulthead

        summ = 0
        while node is not None:
            if node.val == 0 and summ != 0:
                resultnode.next = ListNode(summ)
                resultnode = resultnode.next
                summ = 0
            summ += node.val
            node = node.next


        return resulthead.next 