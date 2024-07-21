class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lst1, lst2 = [], []

        def traversal(root, lst):
            if not root:
                return False

            l = traversal(root.left, lst)
            r = traversal(root.right, lst)

            if not l:
                if not r:
                    lst.append(root.val)
            return True

        traversal(root1, lst1)
        traversal(root2, lst2)

        if len(lst1) != len(lst2):
            return False

        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False

        return True