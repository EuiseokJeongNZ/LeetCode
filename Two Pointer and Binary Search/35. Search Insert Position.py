class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lt = 0
        rt = len(nums) - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if nums[mid] < target:
                lt = mid + 1
            elif nums[mid] > target:
                rt = mid - 1
            else:
                return mid
        return lt # if there is no search of target, return lt