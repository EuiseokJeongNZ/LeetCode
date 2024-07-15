class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        sum = 0
        for num, cnt in dic.items():
            if cnt == 1:
                sum += num

        return sum



