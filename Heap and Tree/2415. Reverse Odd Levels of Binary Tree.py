class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(l, r, depth):
            if l == None or r == None:
                return
            if depth % 2 == 1:
                temp = l.val
                l.val = r.val
                r.val = temp

            traversal(l.left, r.right, depth + 1)
            traversal(r.left, l.right, depth + 1)

        traversal(root.left, root.right, 1)
        return root

