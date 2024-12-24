class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0

        for i in range(n-2):
            f, s, t = nums[i], nums[i+1], nums[i+2]
            if (f+t != 0 and s/(f+t) == 2) or (f+t==0 and s == 0):
                cnt += 1

        return cnt