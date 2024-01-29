# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorderTraversal(root):
            if not root:
                return
            res.append(root.val)
            inorderTraversal(root.left)
            inorderTraversal(root.right)

        inorderTraversal(root)
        return res

        # Solution with Stack
        # res = []
        # stack = []
        # cur = root

        # while cur or stack:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res