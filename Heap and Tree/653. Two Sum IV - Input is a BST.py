class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def traversal(node, target):
            if not node:
                return
            if (target - node.val) in s:
                Solution.answer = True
                return

            s.add(node.val)
            traversal(node.left, target)
            traversal(node.right, target)

        s = set()
        Solution.answer = False

        traversal(root, k)

        return Solution.answer