# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        curA, curB = headA, headB

        while curA != curB:
            if curA is None:
                curA = headB 
            else:
                curA = curA.next 

            if curB is None:
                curB = headA  
            else:
                curB = curB.next  
        return curA 