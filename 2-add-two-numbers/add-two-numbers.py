# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def _get_num_from_reverse_linkedlist(list_head):
            sum_ = 0
            i = 1
            node = list_head
            while node:
                sum_ += (node.val * i)
                i *= 10
                node = node.next
            return sum_

        num1 = _get_num_from_reverse_linkedlist(l1)
        num2 = _get_num_from_reverse_linkedlist(l2)

        result = num1 + num2

        if result == 0:
            return ListNode(0)

        result_head = ListNode()
        current = result_head

        while result > 0:
            digit = result % 10
            current.next = ListNode(digit)
            current = current.next
            result = result // 10

        return result_head.next