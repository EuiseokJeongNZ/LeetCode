# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        res = ListNode(0, None)
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next

        lst.reverse()
        temp = res

        for i in lst:
            ilst = ListNode(i, None)
            temp.next = ilst
            temp = temp.next

        return res.next

        # Someone's Answer
        # new_list = None
        # current = head

        # while current:
        #     next_node = current.next
        #     current.next = new_list
        #     new_list = current
        #     current = next_node

        # return new_list
