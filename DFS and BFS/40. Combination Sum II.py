class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, remaining, lst):
            if remaining == 0:
                temp = list(lst)
                res.append(temp)
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # idea of skip duplicates that i didn't consider
                if start < i and candidates[i] == candidates[i - 1]:
                    continue
                #
                if candidates[i] > target:
                    break
                lst.append(candidates[i])
                dfs(i + 1, remaining - candidates[i], lst)
                lst.pop()

        res = []
        candidates.sort()
        dfs(0, target, [])
        return res
