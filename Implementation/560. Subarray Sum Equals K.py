from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        cnt = 0
        counter = Counter()
        counter[prefix] = 1

        for i in range(n):
            prefix += nums[i]
            if prefix - k in counter:
                cnt += counter[prefix - k]
            counter[prefix] += 1

        return cnt