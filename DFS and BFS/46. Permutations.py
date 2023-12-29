class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = len(nums)

        res = [0] * r
        check = [False] * len(nums)
        answer = []

        def dfs(start):
            if start == r:
                answer.append(list(res))
            else:
                for i in range(len(nums)):
                    if not check[i]:
                        res[start] = nums[i]
                        check[i] = True
                        dfs(start + 1)
                        check[i] = False

        dfs(0)
        return answer