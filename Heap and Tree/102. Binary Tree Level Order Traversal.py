class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traversal(node, depth):
            if not node:
                return

            if not depth in self.dic:
                self.dic[depth] = [node.val]
            else:
                self.dic[depth].append(node.val)
            traversal(node.left, depth + 1)
            traversal(node.right, depth + 1)

        self.dic = {}
        traversal(root, 1)

        return list(self.dic.values())