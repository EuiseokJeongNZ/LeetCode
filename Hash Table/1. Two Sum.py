# My Answer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rtype = []
        temp = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                temp = nums[i] + nums[j]

                if temp == target and i != j:
                    rtype.append(i)
                    rtype.append(j)
                    return rtype

# Someone's Answer
# Using the dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            if n in dict:
                return dict[n], i
            else:
                dict[target-n] = i
