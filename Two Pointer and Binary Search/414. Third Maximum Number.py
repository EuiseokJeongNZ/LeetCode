class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 2:
            nums.sort()
            return nums[1]
        if len(nums) == 1:
            return nums[0]

        temp = [-inf, -inf, -inf]  # infinite

        for i in nums:
            if temp[0] < i and not i in temp:
                temp[2] = temp[1]
                temp[1] = temp[0]
                temp[0] = i
            elif temp[1] < i and not i in temp:
                temp[2] = temp[1]
                temp[1] = i
            elif temp[2] < i and not i in temp:
                temp[2] = i
        temp.sort()

        if -inf in temp:
            return temp[2]

        return temp[0]