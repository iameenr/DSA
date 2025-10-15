# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# [lesser_that_already_present, lesser added from right, greater already present, x, rest of items]

class Solution(object):
  def partition(self, head, x):
    lesser_list_head = lesser_list = ListNode(0)
    greater_list_head = greater_list = ListNode(0)

    while head:
      if head.val < x:
        lesser_list.next = head
        lesser_list = lesser_list.next
      else:
        greater_list.next = head
        greater_list = greater_list.next
      head = head.next
        
    greater_list.next = None
    lesser_list.next = greater_list_head.next
    return lesser_list_head.next
        