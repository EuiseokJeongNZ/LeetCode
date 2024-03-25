class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        find = head
        while find and find.next:
            head = head.next
            find = find.next.next
            if head is find:
                return True
        return False
