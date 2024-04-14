class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        self.answer = 0

        def leftSum(node):
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                self.answer += node.left.val
            leftSum(node.left)
            leftSum(node.right)
            return

        leftSum(root)

        return self.answer
