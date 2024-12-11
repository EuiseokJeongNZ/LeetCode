class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        dic = {chr(ord('a') + i): i for i in range(26)}
        n = len(s)
        min_cost = 0

        for i in range(n):
            index_s = dic[s[i]]
            index_t = dic[t[i]]

            if index_s >= index_t:
                p1 = sum(nextCost[index_s:]) + sum(nextCost[:index_t])
                p2 = sum(previousCost[index_t + 1:index_s + 1])
                min_cost += min(p1, p2)
            else:
                p1 = sum(previousCost[:index_s + 1]) + sum(previousCost[index_t + 1:])
                p2 = sum(nextCost[index_s:index_t])
                min_cost += min(p1, p2)

        return min_cost