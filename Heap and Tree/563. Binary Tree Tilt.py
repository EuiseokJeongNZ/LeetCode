# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tiltSum = 0

        def tilt(node):
            if not node:
                return 0

            leftSum = tilt(node.left)
            rightSum = tilt(node.right)
            self.tiltSum += abs(leftSum - rightSum)

            return node.val + leftSum + rightSum

        tilt(root)

        return self.tiltSum