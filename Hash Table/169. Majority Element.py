class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        max_value = max(dic, key=dic.get)
        return max_value
