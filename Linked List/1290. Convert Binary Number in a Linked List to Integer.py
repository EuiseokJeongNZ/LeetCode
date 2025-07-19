class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = ''
        temp = head

        while temp:
            ans += str(temp.val)
            temp = temp.next

        return int(ans, 2)