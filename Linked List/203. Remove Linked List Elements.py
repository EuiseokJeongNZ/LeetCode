# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            if current.val == val:
                if previous:
                    previous.next = current.next
                else:
                    head = current.next
                current = current.next
            else:
                previous = current
                current = current.next

        return head

        # Someone's Solution
        # dummy = ListNode(0)
        # dummy.next = head

        # current = dummy

        # while current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #     else:
        #         current = current.next

        # return dummy.next

