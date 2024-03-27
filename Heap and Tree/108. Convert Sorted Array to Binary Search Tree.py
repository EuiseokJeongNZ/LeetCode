class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # def listToTree(lst):
        #     if not lst:
        #         return None
        #
        #     mid = len(lst) // 2
        #     root = TreeNode(lst[mid])
        #     root.left = listToTree(lst[:mid])
        #     root.right = listToTree(lst[mid + 1:])
        #     return root
        #
        # return listToTree(nums)

        # Other Solution
        def listToTree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = listToTree(left, mid - 1)
            root.right = listToTree(mid + 1, right)
            return root

        return listToTree(0, len(nums) - 1)