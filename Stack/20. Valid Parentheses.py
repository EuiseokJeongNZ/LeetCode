# My Answer
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        s = deque(s)
        stack = deque()

        while s:
            if s[0] == '(' or s[0] == '{' or s[0] == '[':
                temp = s.popleft()
                stack.append(temp)

            try:
                if s[0] == ')':
                    temp = stack.pop()
                    s.popleft()
                    if temp != '(':
                        return False
                elif s[0] == '}':
                    temp = stack.pop()
                    s.popleft()
                    if temp != '{':
                        return False
                elif s[0] == ']':
                    temp = stack.pop()
                    s.popleft()
                    if temp != '[':
                        return False
            except:
                return False

        if len(stack) != 0:
            return False

        return True

# Someone's Answer
# Given a string that only contains the
# characters (, ), {, }, [, ], determine
# if the input string is valid
def isValid(s):
    stack = [] # only use append and pop
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for bracket in s:
        if bracket in pairs: # pairs' key
            stack.append(bracket)
        elif len(stack) == 0 or \
            bracket != pairs[stack.pop()]:
            return False
    return len(stack) == 0