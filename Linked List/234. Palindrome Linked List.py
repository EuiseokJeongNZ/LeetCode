from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        stack = []
        queue = deque([])

        while current:
            stack.append(str(current.val))
            queue.appendleft(str(current.val))
            current = current.next

        return list(queue) == stack