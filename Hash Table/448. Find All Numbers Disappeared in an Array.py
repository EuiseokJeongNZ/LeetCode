class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        dic = {i: 1 for i in nums}
        start = 0
        for i in range(1, len(nums) + 1):
            if not i in dic:
                res.append(i)
        return res

