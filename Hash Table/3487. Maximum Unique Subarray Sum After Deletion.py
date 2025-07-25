from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        flag = False

        dic = defaultdict(int)
        ans = float('-inf')

        for num in nums:
            if num > 0:
                flag = True
            dic[num] += 1

        if not flag:
            for num in dic.keys():
                ans = max(ans, num)
        else:
            ans = 0
            for num in dic.keys():
                if num > 0:
                    ans += num

        return ans
