# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

        # Solution with Stack
        # res = []
        # stack = []
        # cur = root
        # prev = None

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack[-1]

        #     if cur.right is None or cur.right == prev:
        #         res.append(cur.val)
        #         stack.pop()
        #         prev = cur
        #         cur = None
        #     else:
        #         cur = cur.right

        # return res