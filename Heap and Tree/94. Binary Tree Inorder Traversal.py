# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursion
        res = []

        def inorderTraversal(root):
            if not root:
                return
            inorderTraversal(root.left)
            res.append(root.val)
            inorderTraversal(root.right)

        inorderTraversal(root)
        return res

        # Stack
        # res = []
        # stack = []
        # cur = root

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     cur = cur.right
        # return res
