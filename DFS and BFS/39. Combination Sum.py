class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        lst = []

        def dfs(start):
            if sum(lst) > target:
                return
            elif sum(lst) == target:
                res.append(list(lst))
                return

            for i in range(start, len(candidates)):
                lst.append(candidates[i])
                dfs(i)
                lst.pop()
            return

        dfs(0)
        return res