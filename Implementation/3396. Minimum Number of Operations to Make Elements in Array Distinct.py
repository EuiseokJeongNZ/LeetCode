class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0

        while nums:
            dic = {i: nums.count(i) for i in nums}
            flag = False

            for k, v in dic.items():
                if v == 1:
                    flag = True
                else:
                    flag = False
                    break

            if flag:
                break
            else:
                nums = nums[3:]
                cnt += 1

        return cnt
