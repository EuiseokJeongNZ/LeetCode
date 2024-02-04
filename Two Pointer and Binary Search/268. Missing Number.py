class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        nums.sort()
        for _ in range(len(nums)+1):
            lt = 0
            rt = len(nums)-1
            find = False
            while lt<=rt:
                mid=(lt+rt)//2
                if nums[mid] < target:
                    lt = mid+1
                elif nums[mid] > target:
                    rt = mid-1
                else:
                    find = True
                    break
            if not find:
                return target
            else:
                target += 1