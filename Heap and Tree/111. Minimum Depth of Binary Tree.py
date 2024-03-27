class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0

        def minimum(root, depth):
            if not root:
                return 0
            left = minimum(root.left, depth)
            right = minimum(root.right, depth)

            if left == 0:
                return right + 1
            elif right == 0:
                return left + 1
            else:
                return 1 + min(left, right)

        return minimum(root, depth)
