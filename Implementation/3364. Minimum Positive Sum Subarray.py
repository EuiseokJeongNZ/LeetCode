class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = inf
        n = len(nums)

        for size in range(l, r + 1):
            for start in range(n - size + 1):
                subarray_sum = sum(nums[start:start + size])
                if 0 < subarray_sum < min_sum:
                    min_sum = subarray_sum

        if min_sum == inf:
            return -1

        return min_sum