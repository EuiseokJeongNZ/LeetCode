# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        lst2 = []
        cur1 = l1
        cur2 = l2

        while cur1:
            lst1.append(str(cur1.val))
            cur1 = cur1.next

        while cur2:
            lst2.append(str(cur2.val))
            cur2 = cur2.next

        num1 = int(''.join(lst1)[::-1])
        num2 = int(''.join(lst2)[::-1])
        answer = str(num1 + num2)[::-1]

        res = ListNode(0, None)
        temp = res

        for i in answer:
            cur = ListNode(int(i), None)
            temp.next = cur
            temp = temp.next

        return res.next