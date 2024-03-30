class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findSum(node, currentSum):
            if not node:
                return False
            currentSum += node.val
            if not node.left and not node.right:
                return currentSum == targetSum
            return findSum(node.left, currentSum) or findSum(node.right, currentSum)

        return findSum(root, 0)