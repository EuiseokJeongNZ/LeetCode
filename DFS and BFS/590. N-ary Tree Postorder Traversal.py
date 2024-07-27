class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        self.ans = []

        def traversal(node):
            if not node:
                return
            for next in node.children:
                traversal(next)
            self.ans.append(node.val)

        traversal(root)

        return self.ans