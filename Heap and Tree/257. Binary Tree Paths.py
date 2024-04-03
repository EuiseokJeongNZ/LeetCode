class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        def traverse(node, path, paths):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                paths.append("->".join(path))

            traverse(node.left, path, paths)
            traverse(node.right, path, paths)
            path.pop()
            return

        answer = []
        traverse(root, [], answer)
        return answer
