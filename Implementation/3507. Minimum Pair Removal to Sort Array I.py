class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(lst):
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    return False
            return True

        cnt = 0

        while not check(nums):
            min_sum = float('inf')
            remove_idx = -1

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    remove_idx = i

            nums = nums[:remove_idx] + [nums[remove_idx] + nums[remove_idx + 1]] + nums[remove_idx + 2:]
            cnt += 1

            if len(nums) <= 1:
                break

        return cnt

