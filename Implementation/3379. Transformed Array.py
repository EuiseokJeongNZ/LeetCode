class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            j = nums[i]

            if j > 0 or j < 0:
                res[i] = nums[(i + j) % n]
            else:
                res[i] = nums[i]

        return res