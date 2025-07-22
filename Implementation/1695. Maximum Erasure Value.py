class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, curr = 0, 0
        check = set()
        left = 0

        for right in range(len(nums)):
            while nums[right] in check:
                check.remove(nums[left])
                curr -= nums[left]
                left += 1

            check.add(nums[right])
            curr += nums[right]
            ans = max(ans, curr)

        return ans