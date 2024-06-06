class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node):
            if not node:
                return

            if not node.val in dic:
                dic[node.val] = 1
            else:
                dic[node.val] += 1

            traversal(node.left)
            traversal(node.right)

            return

        dic = {}
        lst = []
        traversal(root)

        max_value = max(list(dic.values()))

        for k, v in dic.items():
            if v == max_value:
                lst.append(k)

        return lst