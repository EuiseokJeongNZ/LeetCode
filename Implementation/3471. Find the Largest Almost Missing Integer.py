from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return -1

        subarrays = []
        for i in range(n - k + 1):
            subarrays.append(nums[i:i + k])

        count = Counter()
        for sub in subarrays:
            count.update(set(sub))  # add and update values to the existing counter

        ans = -1
        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans
