class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        self.max = 0

        # dfs
        def traversal(node, depth):
            if not node.children:
                self.max = max(self.max, depth)
                return
            for next in node.children:
                traversal(next, depth + 1)
            return

        traversal(root, 1)

        # bfs

        # node = deque()
        # node.append((root, 1))
        # self.max = 0
        # while node:
        #     cur, val = node.popleft()
        #     self.max = val
        #     if cur.children:
        #         for child in cur.children:
        #             node.append((child, val+1))

        return self.max