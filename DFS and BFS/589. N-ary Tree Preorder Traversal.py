from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        ans = []

        # dfs

        # def traversal(node):
        #     if not node:
        #         return
        #     ans.append(node.val)
        #     for next in node.children:
        #         traversal(next)

        # traversal(root)

        node = deque()
        node.append(root)

        while node:
            cur = node.popleft()
            ans.append(cur.val)
            if cur.children:
                for child in cur.children[::-1]:
                    node.appendleft(child)

        return ans
