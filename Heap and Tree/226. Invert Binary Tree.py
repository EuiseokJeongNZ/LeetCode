class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def invert(node):
            if not node:
                return

            invert(node.left)
            invert(node.right)

            if not node.left:
                node.left, node.right = node.right, None
                return
            if not node.right:
                node.right, node.left = node.left, None
                return

            node.left, node.right = node.right, node.left

        invert(root)

        return root
