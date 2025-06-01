from itertools import combinations
from math import prod


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total_product = prod(nums)
        n = len(nums)

        if total_product != target * target:
            return False

        for size in range(1, n):
            for indices in combinations(range(n), size):
                product = 1
                for i in indices:
                    product *= nums[i]
                if product == target:
                    return True

        return False

