# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lst = []

        def inorder_count(root):
            if not root:
                return

            inorder_count(root.left)
            lst.append(root.val)
            inorder_count(root.right)

        inorder_count(root)

        return len(lst)