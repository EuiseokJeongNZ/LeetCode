class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []

        def traversal(node):
            if not node:
                return
            lst.append(node.val)
            traversal(node.left)
            traversal(node.right)
            return

        traversal(root)

        lst.sort()
        ans = float('inf')

        for i in range(1, len(lst)):
            temp = abs(lst[i] - lst[i - 1])
            if temp < ans:
                ans = temp

        return ans