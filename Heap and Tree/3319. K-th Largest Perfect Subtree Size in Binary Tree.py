class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []

        def traversal(node):
            if not node:
                return 0, True

            left_size, is_left_perfect = traversal(node.left)
            right_size, is_right_perfect = traversal(node.right)

            if is_left_perfect and is_right_perfect and left_size == right_size:
                size = left_size + right_size + 1
                self.res.append(size)
                return size, True

            return 0, False

        traversal(root)

        self.res.sort(reverse=True)

        return self.res[k - 1] if k <= len(self.res) else -1

