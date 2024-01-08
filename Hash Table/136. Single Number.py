class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for num, count in dic.items():
            if count == 1:
                return num