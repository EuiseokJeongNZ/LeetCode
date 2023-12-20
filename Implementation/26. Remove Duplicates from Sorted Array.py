# Solution with slicing
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

# Solution with two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:  # if nums array is null, return 0
            return 0

        # two pointers each index and i variable
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i + 1]
                index += 1
        return index
