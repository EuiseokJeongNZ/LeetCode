class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
                continue
            i += 1
            j += 1
