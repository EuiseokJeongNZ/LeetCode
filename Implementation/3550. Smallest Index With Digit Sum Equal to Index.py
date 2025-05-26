class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        min_i = float('inf')

        for i, num in enumerate(nums):
            temp = sum(list(map(int, str(num))))
            if temp == i and i < min_i:
                min_i = i

        if min_i == float('inf'):
            return -1

        return min_i