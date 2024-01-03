class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        res = ListNode(0, head)
        cur = head
        while head:
            if cur.val != head.val:
                cur.next = head
                cur = head
            head = head.next
        cur.next = None
        return res.next
