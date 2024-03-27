class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        answer = []

        def traversal(root, depth):
            if not root:
                return
            traversal(root.left, depth + 1)
            answer.append(depth)
            traversal(root.right, depth + 1)

        traversal(root, 1)
        return max(answer)

        # Other Solution
        # if not root:
        #     return 0

        # def traversal(root, depth):
        #     if not root:
        #         return 0
        #     leftDepth = traversal(root.left, depth)
        #     rightDepth = traversal(root.right, depth)
        #     return 1 + max(leftDepth, rightDepth)
        
        # answer = traversal(root, 0)
        # return answer
