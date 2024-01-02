class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        cur = None
        while head:
            if not cur or cur.val != head.val:
                if not res:
                    res = ListNode(head.val)
                    cur = res
                else:
                    cur.next = ListNode(head.val)
                    cur = cur.next
            head = head.next
        return res

        '''
        # simple answer
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        '''
