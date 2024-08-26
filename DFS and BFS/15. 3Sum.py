class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    # missed this part
                    while j < k and nums[j] == nums[j + 1]:  # skip for same value in nums
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:  # skip for same value in nums
                        k -= 1
                    # missed this part

                    j += 1
                    k -= 1

        return res

        # wrong approach that i tried solve it with backtracking

        # def dfs(start, lst):
        #     if len(lst) == 3 and sum(lst) == 0:
        #         temp = []]
        #         for i in range(len(check)):
        #             if check[i]:
        #                 temp.append(nums[i])
        #             temp.sort()
        #         if len(temp) == 3 and not temp in res:
        #             res.append(temp)
        #         return
        #     if start > len(nums)-1:
        #         return

        #     lst.append(nums[start])
        #     check[start] = True
        #     dfs(start + 1, lst)
        #     lst.pop()
        #     check[start] = False
        #     dfs(start + 1, lst)

        # res = []
        # check = [False]*len(nums)
        # dfs(0, [])

        # return res

