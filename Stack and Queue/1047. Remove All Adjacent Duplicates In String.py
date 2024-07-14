from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        s = deque(s)

        stack.append(s.popleft())
        while s:
            if stack and stack[-1] == s[0]:
                stack.pop()
                s.popleft()
            else:
                stack.append(s.popleft())

        return ''.join(stack)