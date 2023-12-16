# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()  # create dummy for result
        current = res  # current node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: # list2.val <= list1.val
                current.next = list2
                list2 = list2.next
            current = current.next

        # execute rest of node
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return res.next  # from next node is the answer