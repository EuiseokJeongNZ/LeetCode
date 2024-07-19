class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None

        def find(root):
            if not root:
                return

            find(root.left)
            find(root.right)
            if root.val == val:
                self.ans = root
                return

        find(root)
        return self.ans