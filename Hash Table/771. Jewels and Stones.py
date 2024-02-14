class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        dic_s = {}

        for i in stones:
            if not i in dic_s:
                dic_s[i] = 1
            else:
                dic_s[i] += 1

        for i in jewels:
            if i in dic_s:
                res += dic_s[i]

        return res
