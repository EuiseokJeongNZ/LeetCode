class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            diameterWholeNode = left + right

            self.diameter = max(self.diameter, diameterWholeNode)

            return max(left, right) + 1

        depth(root)
        return self.diameter
