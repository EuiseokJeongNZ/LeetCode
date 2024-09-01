class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        temp = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            temp = temp.next

        temp.next = temp.next.next

        return res.next