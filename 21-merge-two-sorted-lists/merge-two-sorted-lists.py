class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        head = ListNode(0); dummy = head

        while list1 and list2:
            if list1.val <= list2.val: 
                head.next = list1
                list1 = list1.next
            else: 
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1 is None: head.next = list2
        if list2 is None: head.next = list1

        return dummy.next
        