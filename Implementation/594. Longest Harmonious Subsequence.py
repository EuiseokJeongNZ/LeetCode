class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l, r, res = 0, 1, 0

        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff == 1:
                res = max(res, r - l + 1)
                r += 1
            elif diff < 1:
                r += 1
            else:
                l += 1

        return res