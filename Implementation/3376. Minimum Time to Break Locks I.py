from itertools import permutations


class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        def cal(s):
            res = 0
            x = 1
            for val in s:
                req = math.ceil(val / x)
                res += req
                x += K
            return res

        val = float('inf')
        for s in permutations(strength):
            val = min(val, cal(s))

        return val