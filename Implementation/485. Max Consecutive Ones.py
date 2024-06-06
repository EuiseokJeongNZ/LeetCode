class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        lst = []

        for i in range(len(nums)):
            if nums[i] == 0:
                lst.append(cnt)
                cnt = 0
            elif i == len(nums) - 1 and nums[i] == 1:
                cnt += 1
                lst.append(cnt)
            else:
                cnt += 1

        return max(lst)